from system_design.python_introduction.final_project.src.engine import BacktestEngine

# ====================================================
# main
# ====================================================

if __name__ == "__main__":
    # Indicate the path of the csv files
    engine = BacktestEngine(
        price_file="system_design/python_introduction/final_project/data/coin_all_prices_full.csv",
        universe_file="system_design/python_introduction/final_project/data/coin_universe_150K_40.csv",  # 如果沒有就設成 None
        testing_start="2021-09-26 00:00:00",
        testing_end="2022-09-25 23:00:00",
        window_size=240,
    )
    engine.run()
