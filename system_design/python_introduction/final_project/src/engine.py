import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional
from system_design.python_introduction.final_project.src.datafeed import DataFeed
from system_design.python_introduction.final_project.src.calc_engine import (
    CalculationEngine,
)
from system_design.python_introduction.final_project.src.strategy import (
    SignalGenerator,
    Strategy,
)
from system_design.python_introduction.final_project.src.order_process import OrderProcess
from system_design.python_introduction.final_project.src.inventory import InventoryManager
from system_design.python_introduction.final_project.src.logger import Logger
from system_design.python_introduction.final_project.src.reporter import Reporter

# ====================================================
# 8. BacktestEngine - tie everything together
# ====================================================


@dataclass
class BacktestEngine:
    price_file: str
    universe_file: Optional[str] = None
    testing_start: str = "2021-09-26 00:00:00"
    testing_end: str = "2022-09-25 23:00:00"
    window_size: int = 240

    def run(self):
        # ---- Initialize modules ----
        datafeed = DataFeed(self.price_file, self.universe_file)
        price_panel = datafeed.get_price_panel(self.testing_start, self.testing_end)
        returns_all = datafeed.compute_returns(price_panel)
        tokens_all = list(price_panel.columns)

        calc_engine = CalculationEngine(window_size=self.window_size, n_factors=2)
        signal_gen = SignalGenerator()
        strategy = Strategy(calc_engine, signal_gen)
        order_proc = OrderProcess()
        inventory = InventoryManager(tokens_all)
        logger = Logger()

        timestamps = returns_all.index[self.window_size :]  # From the window starts
        prev_positions = pd.Series(0, index=tokens_all, dtype=float)

        for t in timestamps:
            universe_tokens = datafeed.get_universe_tokens(t, tokens_all)
            new_positions, diag = strategy.step(
                returns_all, t, universe_tokens, prev_positions
            )

            # Orders & filled (fully filled)
            orders = order_proc.generate_orders(prev_positions, new_positions)
            filled_positions = order_proc.execute_orders(new_positions)

            # Update inventory; use current returns as pnl basis
            ret_row = returns_all.loc[t]
            inventory.update(t, filled_positions, ret_row)

            # logging
            logger.log_eigen_Q(t, diag["tokens_Q"], diag["Q"])
            logger.log_signals(t, filled_positions)
            logger.log_s_scores(t, diag["s_scores"])

            prev_positions = filled_positions

        # Write to csv
        logger.save_all()

        # Report & performance
        reporter = Reporter(inventory, logger)
        reporter.plot_equity_and_hist()
        reporter.plot_s_scores(tokens=["BTC", "ETH"])  # Task 3 two plots
