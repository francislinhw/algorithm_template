import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional

# ====================================================
# 2. CalculationEngine - PCA, regression, OU, s-score
# ====================================================


@dataclass
class OUParams:
    kappa: float
    m: float
    sigma: float
    sigma_eq: float


class CalculationEngine:
    def __init__(self, window_size: int = 240, n_factors: int = 2):
        self.window_size = window_size
        self.n_factors = n_factors

    # ---------- PCA ----------
    def _fit_pca(
        self, window: pd.DataFrame
    ) -> Tuple[np.ndarray, np.ndarray, pd.DataFrame]:
        """
        window: (M, N) returns (may have NaN)
        Returns:
            eigenvectors: (n_factors, K)
            vol_vec: (K,)
            window_clean: (M, K) cleaned window that matches the eigenvectors
        """
        # Use a new variable, don't touch the outer window
        w = window.copy()

        # Handle NaN & inf
        w = w.replace([np.inf, -np.inf], np.nan)
        # Drop columns with too many NaN
        w = w.dropna(axis=1, thresh=int(0.8 * len(w)))
        # Fill the remaining NaN with 0 (equal to no action)
        w = w.fillna(0.0)

        # If after cleaning, there's only 1 column, can't do PCA
        if w.shape[1] < 2:
            raise ValueError("Not enough valid tokens for PCA")

        vol_vec = w.std(axis=0).values
        vol_vec[vol_vec == 0] = 1e-8

        X = w.values
        X_std = (X - X.mean(axis=0)) / (X.std(axis=0) + 1e-8)

        pca = PCA(n_components=self.n_factors)
        pca.fit(X_std)
        eigenvectors = pca.components_  # (n_factors, K)

        return eigenvectors, vol_vec, w

    def _eigen_portfolios(
        self, eigenvectors: np.ndarray, vol_vec: np.ndarray
    ) -> np.ndarray:
        """
        Q_{j,i} = v_{j,i} / sigma_i
        """
        Q = eigenvectors / (vol_vec[None, :] + 1e-8)
        return Q  # shape (n_factors, K)

    def _factor_returns(self, window: pd.DataFrame, Q: np.ndarray) -> pd.DataFrame:
        # The window here must be the same as the cleaned window used in PCA
        X = window.values  # (M, K)
        F = X @ Q.T  # (M, n_factors)
        F_df = pd.DataFrame(
            F, index=window.index, columns=[f"F{j+1}" for j in range(Q.shape[0])]
        )
        return F_df

    # ---------- Regression + OU ----------
    @staticmethod
    def _regress_residuals(r_i: pd.Series, F: pd.DataFrame) -> pd.Series:
        y = r_i.values.reshape(-1, 1)
        X = np.column_stack([np.ones(len(F)), F.values])
        beta_hat = np.linalg.inv(X.T @ X) @ (X.T @ y)
        y_hat = (X @ beta_hat).flatten()
        eps = r_i - y_hat
        return pd.Series(eps, index=r_i.index)

    @staticmethod
    def _fit_ou_from_X(X: pd.Series, dt: float = 1.0 / 8760) -> Optional[OUParams]:
        if len(X) < 10:
            return None
        X_l = X.values[:-1]
        X_next = X.values[1:]
        n = len(X_l)
        design = np.column_stack([np.ones(n), X_l])
        beta = np.linalg.inv(design.T @ design) @ (design.T @ X_next)
        a, b = beta.tolist()

        eta = X_next - design @ beta
        sigma_eta = eta.std(ddof=1)
        if sigma_eta == 0:
            return None

        # Safe handling of b
        if b <= 0 or b >= 1:
            b = min(max(b, 1e-6), 0.999999)

        kappa = -np.log(b) / dt
        m = a / (1 - b)
        sigma = np.sqrt(2 * kappa * sigma_eta**2 / (1 - np.exp(-2 * kappa * dt) + 1e-12))
        sigma_eq = sigma / np.sqrt(2 * kappa + 1e-12)
        return OUParams(kappa=kappa, m=m, sigma=sigma, sigma_eq=sigma_eq)

    # ---------- Main entry ----------
    def compute(
        self,
        returns_all: pd.DataFrame,
        t: pd.Timestamp,
        universe_tokens: List[str],
    ) -> Dict:
        """
        Calculation process at time t:
        - Get window (only take universe tokens)
        - PCA (do on cleaned window tokens)
        - Eigen-portfolios (dimension must be consistent)
        - Factor returns F
        - Regress each token, OU, s-score
        """

        # Step 1: Get window (may have NaN)
        window = returns_all.loc[:t, universe_tokens].tail(self.window_size).copy()

        if window.shape[0] < self.window_size // 2 or window.shape[1] == 0:
            return {"Q": None, "F": None, "s_scores": {}}

        # Step 2: PCA, only do on cleaned window
        try:
            eigenvectors, vol_vec, window_clean = self._fit_pca(window)
        except ValueError:
            return {"Q": None, "F": None, "s_scores": {}}

        # Step 3: Group eigen-portfolios
        Q = self._eigen_portfolios(eigenvectors, vol_vec)

        # Debug (if needed, can leave it)
        # print("window_clean shape:", window_clean.shape)
        # print("Q shape:", Q.shape)

        # Step 4: Factor returns（用同一份 cleaned window）
        F = self._factor_returns(window_clean, Q)

        # Step 5: Regress each token, OU
        s_scores: Dict[str, float] = {}
        ou_params: Dict[str, OUParams] = {}

        for token in window_clean.columns:
            r_i = window_clean[token].dropna()
            if len(r_i) < int(0.8 * len(window_clean)):
                continue

            F_i = F.loc[r_i.index]
            eps = self._regress_residuals(r_i, F_i)
            X = eps.cumsum()

            ou = self._fit_ou_from_X(X)
            if ou is None or ou.sigma_eq == 0:
                continue

            s_val = (X.iloc[-1] - ou.m) / (ou.sigma_eq + 1e-12)
            s_scores[token] = s_val
            ou_params[token] = ou

        return {
            "Q": Q,
            "tokens": list(window_clean.columns),
            "F": F,
            "s_scores": s_scores,
            "ou_params": ou_params,
        }
