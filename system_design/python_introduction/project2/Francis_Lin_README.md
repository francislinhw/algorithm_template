# Stock Market Prediction and Trading Strategy Project

This repository contains Python code for predicting stock price movements and evaluating trading strategies using machine learning models and technical indicators.

## Project Structure

```
.
├── Francis_Lin_task1.py          # Task 1 machine learning model
├── Francis_Lin_project2.py       # Main project: ML models, feature engineering, and backtesting
├── tickers.csv                   # List of tickers used in the project
└── README.md
```

## Features

### Data Processing
- Downloads historical stock data from Yahoo Finance
- Cleans missing values and caps outliers
- Constructs technical indicators such as moving averages, RSI, MACD, Bollinger Bands, volatility, and momentum

### Machine Learning Models
- LassoCV for feature selection and regression-based classification
- LogisticRegressionCV for binary prediction of price movement
- Cross-validation included in both models
- Applies models across multiple stocks and selects the best-performing model

### Expanded Stock Universe
- The selected best ML model is tested on a larger universe of stocks
- Top 10 stocks are selected based on predictive performance

### Trading Strategy Backtesting
- Machine Learning-based trading strategy
- MACD long–short strategy as benchmark
- Backtested using Backtrader with:
  - Portfolio value tracking
  - Sharpe ratio
  - Maximum drawdown
  - Daily returns via PyFolio analyzer

### Output
Running the project generates:
- CSV files summarizing model performance and backtest metrics
- QuantStats HTML reports for the selected stocks

## Installation

Requires Python 3.9+ and the following libraries:

- pandas
- numpy
- scikit-learn
- yfinance
- backtrader
- quantstats
- tqdm

Install using:

```
pip install pandas numpy scikit-learn yfinance backtrader quantstats tqdm
```

## Running the Code

### Task 1
```
python Francis_Lin_task1.py
```

### Project 2
```
python Francis_Lin_project2.py
```

This will execute the full pipeline:
- Data processing
- Model training
- Expanded universe evaluation
- Backtesting
- Report generation

## Notes
- Some stocks may not have enough data; these are skipped automatically
- MACD strategy is implemented in long–short format
- All backtests use a fixed 10% position sizing for consistency
