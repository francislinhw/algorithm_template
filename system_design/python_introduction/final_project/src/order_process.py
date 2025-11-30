import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional

# ====================================================
# 4. OrderProcess - translate positions into orders
# ====================================================


class OrderProcess:
    """
    Assume all orders are fully filled in backtest.
    """

    @staticmethod
    def generate_orders(prev_pos: pd.Series, new_pos: pd.Series) -> pd.Series:
        """
        order = new - prev
        """
        return new_pos - prev_pos

    @staticmethod
    def execute_orders(new_pos: pd.Series) -> pd.Series:
        """
        fully filled
        """
        return new_pos.copy()
