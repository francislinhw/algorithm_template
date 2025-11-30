import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional
from system_design.python_introduction.final_project.src.calc_engine import (
    CalculationEngine,
)

# ====================================================
# 3. Strategy - use s-scores to decide positions
# ====================================================


@dataclass
class SignalGenerator:
    s_bo: float = 1.25
    s_so: float = 1.25
    s_bc: float = 0.75
    s_sc: float = 0.50

    def update_position(self, s: float, prev_pos: int) -> int:
        pos = prev_pos

        # close
        if pos > 0 and s > self.s_bc:
            pos = 0
        elif pos < 0 and s < self.s_sc:
            pos = 0

        # open
        if pos == 0:
            if s < -self.s_bo:
                pos = 1
            elif s > self.s_so:
                pos = -1

        return pos


class Strategy:
    def __init__(self, calc_engine: CalculationEngine, signal_gen: SignalGenerator):
        self.calc_engine = calc_engine
        self.signal_gen = signal_gen

    def step(
        self,
        returns_all: pd.DataFrame,
        t: pd.Timestamp,
        universe_tokens: List[str],
        prev_positions: pd.Series,
    ) -> Tuple[pd.Series, Dict]:
        """
        produce new positions at time t
        """
        calc_res = self.calc_engine.compute(returns_all, t, universe_tokens)
        s_scores = calc_res["s_scores"]
        tokens_in_window = calc_res.get("tokens", universe_tokens)

        new_positions = prev_positions.copy()

        for token in tokens_in_window:
            s_val = s_scores.get(token)
            if s_val is None:
                continue
            prev_pos = prev_positions.get(token, 0)
            new_positions[token] = self.signal_gen.update_position(s_val, prev_pos)

        diagnostics = {
            "Q": calc_res["Q"],
            "tokens_Q": tokens_in_window,
            "s_scores": s_scores,
        }
        return new_positions, diagnostics
