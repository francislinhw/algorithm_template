import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional

# ====================================================
# 6. Logger - save all useful data to disk
# ====================================================


class Logger:
    def __init__(self):
        self.eigen1_records: List[Tuple[pd.Timestamp, Dict[str, float]]] = []
        self.eigen2_records: List[Tuple[pd.Timestamp, Dict[str, float]]] = []
        self.signal_records: List[Tuple[pd.Timestamp, Dict[str, int]]] = []
        self.s_scores_records: Dict[str, List[Tuple[pd.Timestamp, float]]] = {}

    def log_eigen_Q(self, t: pd.Timestamp, tokens: List[str], Q: np.ndarray):
        if Q is None:
            return
        if len(tokens) != Q.shape[1]:
            return
        self.eigen1_records.append((t, dict(zip(tokens, Q[0, :]))))
        if Q.shape[0] > 1:
            self.eigen2_records.append((t, dict(zip(tokens, Q[1, :]))))

    def log_signals(self, t: pd.Timestamp, positions: pd.Series):
        d = {k: int(v) for k, v in positions.items()}
        self.signal_records.append((t, d))

    def log_s_scores(self, t: pd.Timestamp, s_scores: Dict[str, float]):
        for token, s in s_scores.items():
            if token not in self.s_scores_records:
                self.s_scores_records[token] = []
            self.s_scores_records[token].append((t, s))

    # ----- write to csv -----
    def save_task1a(self):
        if self.eigen1_records:
            eig1_df = pd.DataFrame(
                {ts: vec for ts, vec in self.eigen1_records}
            ).T.sort_index()
            eig1_df.to_csv("task1a_1.csv", index_label="timestamp")
        if self.eigen2_records:
            eig2_df = pd.DataFrame(
                {ts: vec for ts, vec in self.eigen2_records}
            ).T.sort_index()
            eig2_df.to_csv("task1a_2.csv", index_label="timestamp")

    def save_trading_signals(self):
        if not self.signal_records:
            return
        sig_df = pd.DataFrame({ts: vec for ts, vec in self.signal_records}).T.sort_index()
        sig_df.to_csv("trading_signal.csv", index_label="timestamp")

    def save_all(self):
        self.save_task1a()
        self.save_trading_signals()
        # s-scores kept in memory for Reporter to plot
        # If needed, can also write out the csv for each token
