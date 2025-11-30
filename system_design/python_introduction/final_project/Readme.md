# Final Project – Statistical Arbitrage Strategy

This repository implements the Avellaneda & Lee (2010) statistical arbitrage model using hourly cryptocurrency data.  
The project follows an object‑oriented architecture and produces all required outputs (CSV + plots).



## Project Requirements
Python 3.10+
Required packages:
- numpy
- pandas
- matplotlib
- scikit-learn

Install all packages:
pip install numpy pandas matplotlib scikit-learn

## 📂 Project Structure

The project structure is as follows: 
```
(under system_design/python_introduction/final_project/)
```
```
system_design/
├── python_introduction/
│   └── final_project/
│       └── In the below folder structure

```
⚠️ Note:  
Please make sure that the folder structure under `system_design/python_introduction/final_project/`  
is preserved exactly as shown, otherwise module imports will fail.




```
final_project/
│
├── data/                     # Raw input data
│   ├── coin_all_prices_full.csv
│   └── coin_universe_150K_40.csv
│
├── results/                  # All generated outputs
│   ├── task1a_1.csv          # Eigen-portfolio 1 weights
│   ├── task1a_2.csv          # Eigen-portfolio 2 weights
│   ├── trading_signal.csv    # Strategy signals
│   ├── cumulative_return.png
│   ├── cumulative_return_4_assets.png
│   ├── hist_return.png
│   ├── s_score_BTC.png
│   ├── s_score_ETH.png
│   ├── eigen_weights_2021-10-07.png
│   ├── eigen_weights_2022-04-15.png
│   └── result_plot.py            # Recreates figures
│
├── src/                      # All modules
│   ├── datafeed.py           # Data loading & returns
│   ├── calc_engine.py        # PCA, regression, OU, s-score
│   ├── engine.py             # Main engine
│   ├── inventory.py          # Inventory manager
│   ├── logger.py             # Logger
│   ├── order_process.py      # Order processing
│   ├── reporter.py           # Reporter
│   └── strategy.py           # Trading rules
│   
├── doc/                      # Documentation
│   └── Final_Rubric_60pts.xlsx # Grading rubric
│   └── Final_Project.pdf       # Question Description
│   └── Statistical_Arbitrage.pdf       # Paper
│
├── main.py                   # Entry point (run full pipeline)
├── ISYE6767_Francis_Lin_Final_Project.pdf.txt          # Final Project Submission
└── README.md                 # This file
```

---

## ▶️ How to Run

```
python main.py
```

All outputs will be saved automatically in the `results/` folder.

---

## ✔️ Included Deliverables
- Final Report (PDF) with plots and analysis!
- PCA eigenvector CSVs (`task1a_1.csv`, `task1a_2.csv`)
- Eigen-portfolio weight plots
- s-score evolution plots (BTC, ETH)
- Trading signal file (`trading_signal.csv`)
- Strategy backtest: cumulative return + histogram
- Sharpe Ratio & Max Drawdown in final report
