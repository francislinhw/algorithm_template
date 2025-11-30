import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional

# ====================================================
# 1. DataFeed - read & preprocess data
# ====================================================


class DataFeed:
    """
    專門處理你的 csv:
    - startTime: datetime (ISO8601)
    - time: unix ms (ignore)
    - 其餘欄位：token prices
    """

    def __init__(self, price_path: str, universe_path: Optional[str] = None):
        self.price_path = price_path
        self.universe_path = universe_path
        self.price_panel_: Optional[pd.DataFrame] = None
        self.universe_: Optional[pd.DataFrame] = None

    def load_prices(self) -> pd.DataFrame:
        if self.price_panel_ is not None:
            return self.price_panel_

        df = pd.read_csv(self.price_path)
        df["startTime"] = pd.to_datetime(df["startTime"])
        df = df.sort_values("startTime").set_index("startTime")

        if "time" in df.columns:
            df = df.drop(columns=["time"])

        df = df.apply(pd.to_numeric, errors="coerce")
        self.price_panel_ = df
        return df

    def load_universe(self) -> Optional[pd.DataFrame]:
        if self.universe_path is None:
            return None
        if self.universe_ is not None:
            return self.universe_

        df = pd.read_csv(self.universe_path)

        # timestamp column name is startTime
        if "startTime" not in df.columns:
            raise ValueError("Universe CSV missing 'startTime' column")

        df["startTime"] = pd.to_datetime(df["startTime"], errors="coerce")
        df["startTime"] = df["startTime"].dt.tz_localize(None)
        df = df.set_index("startTime")

        # Remove time column (millisecond timestamp)
        if "time" in df.columns:
            df = df.drop(columns=["time"])

        self.universe_ = df
        return df

    def get_price_panel(
        self,
        start: Optional[str] = None,
        end: Optional[str] = None,
    ) -> pd.DataFrame:

        df = self.load_prices()

        # --- Ensure index is tz-naive ---
        if df.index.tz is not None:
            df.index = df.index.tz_convert(None)

        # --- Process start ---
        if start is not None:
            start_dt = pd.to_datetime(start)
            # If start has timezone, remove it
            if start_dt.tzinfo is not None:
                start_dt = start_dt.tz_localize(None)
            df = df[df.index >= start_dt]

        # --- Process end ---
        if end is not None:
            end_dt = pd.to_datetime(end)
            if end_dt.tzinfo is not None:
                end_dt = end_dt.tz_localize(None)
            df = df[df.index <= end_dt]

        return df.copy()

    @staticmethod
    def compute_returns(price_panel: pd.DataFrame) -> pd.DataFrame:
        return price_panel.pct_change()

    def get_universe_tokens(self, ts: pd.Timestamp, all_tokens: List[str]) -> List[str]:
        univ = self.load_universe()
        if univ is None:
            return all_tokens

        if ts not in univ.index:
            return all_tokens

        row = univ.loc[ts]

        # The first 0~39 columns are token names
        tokens = [t for t in row.values if isinstance(t, str)]

        # Filter out tokens not in price_panel
        tokens = [t for t in tokens if t in all_tokens]

        return tokens if tokens else all_tokens
