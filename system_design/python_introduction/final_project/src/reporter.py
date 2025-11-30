import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional
from system_design.python_introduction.final_project.src.inventory import InventoryManager
from system_design.python_introduction.final_project.src.logger import Logger

# ====================================================
# 7. Reporter - plots & performance metrics
# ====================================================


class Reporter:
    def __init__(self, inventory: InventoryManager, logger: Logger):
        self.inv = inventory
        self.log = logger

    @staticmethod
    def sharpe_ratio(
        returns: pd.Series, annual_factor: float = np.sqrt(24 * 365)
    ) -> float:
        r = returns.dropna()
        mu = r.mean()
        sig = r.std(ddof=1)
        if sig == 0:
            return 0.0
        return float(mu / sig * annual_factor)

    @staticmethod
    def max_drawdown(equity: pd.Series) -> float:
        running_max = equity.cummax()
        dd = (equity - running_max) / running_max
        return float(dd.min())

    def plot_equity_and_hist(self):
        ret = self.inv.portfolio_returns
        eq = (1 + ret).cumprod()

        # cumulative return
        plt.figure(figsize=(10, 5))
        eq.plot()
        plt.title("Cumulative Return of Stat-Arb Strategy")
        plt.xlabel("Time")
        plt.ylabel("Equity")
        plt.tight_layout()
        plt.savefig("cumulative_return.png")

        # histogram
        plt.figure(figsize=(7, 4))
        ret.hist(bins=50)
        plt.title("Histogram of Hourly Returns")
        plt.xlabel("Return")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig("hist_return.png")

        sr = self.sharpe_ratio(ret)
        mdd = self.max_drawdown(eq)
        print(f"Sharpe ratio: {sr:.3f}")
        print(f"Maximum drawdown (MDD): {mdd:.2%}")

    def plot_s_scores(self, tokens: List[str]):
        for token in tokens:
            if token not in self.log.s_scores_records:
                continue
            times, vals = zip(*self.log.s_scores_records[token])
            plt.figure(figsize=(10, 4))
            plt.plot(times, vals)
            plt.title(f"s-score evolution: {token}")
            plt.xlabel("Time")
            plt.ylabel("s-score")
            plt.tight_layout()
            plt.savefig(f"s_score_{token}.png")
