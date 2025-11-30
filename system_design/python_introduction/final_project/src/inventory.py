import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional

# ====================================================
# 5. InventoryManager - keep track of positions
# ====================================================


class InventoryManager:
    def __init__(self, tokens: List[str]):
        self.tokens = tokens
        self.positions = pd.DataFrame(columns=tokens, dtype=float)
        self.portfolio_returns = pd.Series(dtype=float)

    def update(
        self,
        t: pd.Timestamp,
        filled_pos: pd.Series,
        ret_row: Optional[pd.Series],
    ):
        self.positions.loc[t] = filled_pos.reindex(self.tokens).fillna(0.0)
        if ret_row is not None:
            r = ret_row.reindex(self.tokens).fillna(0.0)
            port_ret = float((self.positions.loc[t] * r).mean())
            self.portfolio_returns.loc[t] = port_ret
        else:
            self.portfolio_returns.loc[t] = 0.0
