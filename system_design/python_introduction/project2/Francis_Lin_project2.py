import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoCV, LogisticRegressionCV
from tqdm import tqdm
from sklearn import metrics
import backtrader as bt
import backtrader.analyzers as btanalyzers
import quantstats
import warnings

warnings.filterwarnings("ignore")


# ----------------------------------------
# Data processing class
# ----------------------------------------
class MarketDataset:
    def __init__(self, ticker):
        self.ticker = ticker
        self.df = pd.DataFrame()

    def load_raw(self):
        """Extract raw data from Yahoo Finance"""
        data = yf.Ticker(self.ticker).history(start="2000-01-01", end="2021-11-13")
        if data.empty:
            self.df = pd.DataFrame()
        else:
            self.df = data[["Open", "High", "Low", "Close", "Volume"]]

    def clean_data(self):
        """Basic data cleaning and outlier handling"""
        if self.df.empty:
            return

        self.df.ffill(inplace=True)
        self.df.bfill(inplace=True)

        for col in self.df.columns:
            if col != "Volume":
                mu = self.df[col].mean()
                sigma = self.df[col].std()
                bound = sigma * 3
                self.df[col] = self.df[col].clip(mu - bound, mu + bound)

        self.df.dropna(inplace=True)

    def build_features(self):
        """Build technical indicators and target"""
        if self.df.empty:
            return

        self.df["ret"] = self.df["Close"].pct_change().fillna(0)

        for win in [5, 10, 20, 50, 100, 200]:
            self.df[f"ma_{win}"] = self.df["Close"].rolling(win).mean()

        price_diff = self.df["Close"].diff()
        gain = price_diff.where(price_diff > 0, 0)
        loss = -price_diff.where(price_diff < 0, 0)
        rs = gain.rolling(14).mean() / loss.rolling(14).mean()
        self.df["rsi"] = 100 - (100 / (1 + rs))

        fast = self.df["Close"].ewm(span=12).mean()
        slow = self.df["Close"].ewm(span=26).mean()
        self.df["macd"] = fast - slow
        self.df["signal"] = self.df["macd"].ewm(span=9).mean()

        mid = self.df["Close"].rolling(20).mean()
        std = self.df["Close"].rolling(20).std()
        self.df["bb_up"] = mid + 2 * std
        self.df["bb_dn"] = mid - 2 * std

        self.df["volatility"] = self.df["ret"].rolling(30).std()
        self.df["momentum"] = self.df["Close"].pct_change(30)

        self.df.dropna(inplace=True)

        self.df["y"] = (self.df["ret"] > 0).astype(int)

        if len(self.df) < 300:
            self.df = pd.DataFrame()

    def split_norm(self):
        """Split data and normalize"""
        if self.df.empty:
            raise ValueError(
                f"[{self.ticker}] Not enough data after feature engineering."
            )

        X = self.df.drop("y", axis=1)
        y = self.df["y"]

        if len(X) < 10:
            raise ValueError(f"[{self.ticker}] Not enough samples to split.")

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.4, shuffle=False
        )

        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(X_train)
        X_test_std = scaler.transform(X_test)

        return X_train_std, y_train.values, X_test_std, y_test.values


# ----------------------------------------
# Model training
# ----------------------------------------
def fit_lasso(X, y):
    model = LassoCV(cv=10, random_state=42)
    model.fit(X, y)
    return model


def fit_logistic(X, y):
    model = LogisticRegressionCV(cv=20, random_state=42)
    model.fit(X, y)
    return model


# ----------------------------------------
# Backtrader data format
# ----------------------------------------
class BtDataFeed(bt.feeds.PandasData):
    lines = ("y", "Close", "Open")
    params = (("y", -1), ("Close", -1), ("Open", -1))


# ----------------------------------------
# Backtrader strategies
# ----------------------------------------
class StrategyML(bt.Strategy):
    params = (("model", None),)

    def next(self):
        if self.datas[0].y[0] == 1 and not self.position:
            self.buy()
        elif self.datas[0].y[0] == -1 and self.position:
            self.sell()


class StrategyMACD_LongShort(bt.Strategy):
    def __init__(self, model=None):
        self.macd = bt.indicators.MACD(
            self.datas[0].close,
            period_me1=12,
            period_me2=26,
            period_signal=9,
        )
        self.cross = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)

    def next(self):
        # Cross over → Long
        if self.cross > 0:
            # If currently short → Close short position
            if self.position.size < 0:
                self.close()
            # If no position → Open long position
            if self.position.size == 0:
                self.buy()

        # Cross under → Short
        elif self.cross < 0:
            # If currently long → Close long position
            if self.position.size > 0:
                self.close()
            # If no position → Open short position
            if self.position.size == 0:
                self.sell()


# ----------------------------------------
# Backtesting process
# ----------------------------------------
def run_backtest(ds, strategy, model):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy, model=model)

    data_feed = BtDataFeed(dataname=ds.df)
    cerebro.adddata(data_feed)

    cerebro.broker.set_cash(10000)
    cerebro.addsizer(bt.sizers.PercentSizer, percents=10)

    cerebro.addanalyzer(btanalyzers.SharpeRatio, _name="sharpe")
    cerebro.addanalyzer(btanalyzers.DrawDown, _name="drawdown")
    cerebro.addanalyzer(btanalyzers.Returns, _name="returns")
    cerebro.addanalyzer(btanalyzers.PyFolio, _name="pf")

    results = cerebro.run()
    strat = results[0]

    value = cerebro.broker.getvalue()
    sharpe = strat.analyzers.sharpe.get_analysis().get("sharperatio", None)
    dd = strat.analyzers.drawdown.get_analysis()["max"]["drawdown"]
    returns, _, _, _ = strat.analyzers.pf.get_pf_items()

    return {"final_value": value, "sharpe_ratio": sharpe, "max_drawdown": dd}, returns


# ----------------------------------------
# Main program
# ----------------------------------------
if __name__ == "__main__":

    tickers = pd.read_csv("system_design/python_introduction/project2/tickers.csv")[
        "Ticker"
    ].tolist()
    tickers.remove("HIBB")

    best_lasso, best_logi = None, None
    avg_lasso_score = avg_logi_score = 0

    result_small = pd.DataFrame(
        columns=["Lasso_acc", "Lasso_prec", "Logi_acc", "Logi_prec"],
        index=tickers,
    )

    # ----------------------------------------
    # Finding best models
    # ----------------------------------------
    for t in tqdm(tickers, desc="Selecting best models"):
        ds = MarketDataset(t)

        try:
            ds.load_raw()
            ds.clean_data()
            ds.build_features()
            Xtr, ytr, Xte, yte = ds.split_norm()
        except Exception as e:
            print(f"⚠ Skip {t}: {e}")
            continue

        lasso = fit_lasso(Xtr, ytr)
        logi = fit_logistic(Xtr, ytr)

        l_pred = (lasso.predict(Xte) > 0.5).astype(int)
        g_pred = logi.predict(Xte)

        acc_l = metrics.accuracy_score(yte, l_pred)
        prec_l = metrics.precision_score(yte, l_pred)
        acc_g = metrics.accuracy_score(yte, g_pred)
        prec_g = metrics.precision_score(yte, g_pred)

        result_small.loc[t] = [acc_l, prec_l, acc_g, prec_g]

        result_small.to_csv(
            "system_design/python_introduction/project2/Francis_Lin_nine_stocks_result.csv"
        )

        score_l = (acc_l + prec_l) / 2
        score_g = (acc_g + prec_g) / 2

        avg_lasso_score += score_l
        avg_logi_score += score_g

        if best_lasso is None or score_l > avg_lasso_score / len(tickers):
            best_lasso = lasso

        if best_logi is None or score_g > avg_logi_score / len(tickers):
            best_logi = logi

    # ----------------------------------------
    # Expanding universe
    # ----------------------------------------
    universe = [
        "META",
        "AAPL",
        "AMZN",
        "NFLX",
        "GOOG",
        "MSFT",
        "NVDA",
        "DIS",
        "JPM",
        "GS",
        "XOM",
        "PG",
        "KO",
        "MA",
        "WMT",
        "ORCL",
        "MRK",
        "BAC",
        "CVX",
        "AMD",
    ]

    large_result = pd.DataFrame(
        columns=["Lasso_acc", "Lasso_prec", "Logi_acc", "Logi_prec", "Score"],
        index=universe,
    )

    for t in tqdm(universe, desc="Evaluating expanded universe"):
        ds = MarketDataset(t)

        try:
            ds.load_raw()
            ds.clean_data()
            ds.build_features()
            Xtr, ytr, Xte, yte = ds.split_norm()
        except Exception as e:
            print(f"⚠ Skip {t}: {e}")
            continue

        l_pred = (best_lasso.predict(Xte) > 0.5).astype(int)
        g_pred = best_logi.predict(Xte)

        acc_l = metrics.accuracy_score(yte, l_pred)
        prec_l = metrics.precision_score(yte, l_pred)
        acc_g = metrics.accuracy_score(yte, g_pred)
        prec_g = metrics.precision_score(yte, g_pred)

        large_result.loc[t, ["Lasso_acc", "Lasso_prec", "Logi_acc", "Logi_prec"]] = [
            acc_l,
            prec_l,
            acc_g,
            prec_g,
        ]
        large_result.loc[t, "Score"] = (acc_l + prec_l + acc_g + prec_g) / 4

    top10 = large_result.sort_values("Score").head(10)

    backtest_ml = pd.DataFrame(
        columns=["final_value", "sharpe_ratio", "max_drawdown"], index=top10.index
    )
    backtest_macd = backtest_ml.copy()

    # ----------------------------------------
    # Backtesting strategies
    # ----------------------------------------
    for t in tqdm(top10.index, desc="Backtesting strategies"):
        ds = MarketDataset(t)

        try:
            ds.load_raw()
            ds.clean_data()
            ds.build_features()
        except Exception as e:
            print(f"⚠ Skip {t}: {e}")
            continue

        try:
            res1, ret1 = run_backtest(ds, StrategyML, best_logi)
            res2, ret2 = run_backtest(ds, StrategyMACD_LongShort, best_logi)
        except Exception as e:
            print(f"⚠ Backtest failed for {t}: {e}")
            continue

        backtest_ml.loc[t] = res1
        backtest_macd.loc[t] = res2

        quantstats.reports.html(
            ret2,
            output=f"system_design/python_introduction/project2/{t}_report.html",
            title=f"QuantStats Report - {t}",
        )

    backtest_ml.sort_values("sharpe_ratio", ascending=False).to_csv(
        "system_design/python_introduction/project2/Francis_Lin_MLStrategy_by_sharpe_ratio.csv"
    )
    backtest_ml.sort_values("max_drawdown").to_csv(
        "system_design/python_introduction/project2/Francis_Lin_MLStrategy_by_max_drawdown.csv"
    )
    backtest_macd.sort_values("sharpe_ratio", ascending=False).to_csv(
        "system_design/python_introduction/project2/Francis_Lin_MACDCrossoverStrategy_by_sharpe_ratio.csv"
    )
    backtest_macd.sort_values("max_drawdown").to_csv(
        "system_design/python_introduction/project2/Francis_Lin_MACDCrossoverStrategy_by_max_drawdown.csv"
    )
