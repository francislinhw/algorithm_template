import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

price_file = (
    "system_design/python_introduction/final_project/data/coin_all_prices_full.csv"
)
df = pd.read_csv(price_file)
df["startTime"] = pd.to_datetime(df["startTime"]).dt.tz_localize(None)
df = df.set_index("startTime")
if "time" in df.columns:
    df = df.drop(columns=["time"])

# Keep only numeric columns
df = df.apply(pd.to_numeric, errors="coerce")


returns = df.pct_change().dropna()
returns.index = returns.index.tz_localize(None)

eig1 = pd.read_csv(
    "system_design/python_introduction/final_project/results/task1a_1.csv",
    index_col=0,
)
eig2 = pd.read_csv(
    "system_design/python_introduction/final_project/results/task1a_2.csv",
    index_col=0,
)

eig1.index = pd.to_datetime(eig1.index).tz_localize(None)
eig2.index = pd.to_datetime(eig2.index).tz_localize(None)

common_idx = returns.index.intersection(eig1.index)
returns = returns.loc[common_idx]
eig1 = eig1.loc[common_idx]
eig2 = eig2.loc[common_idx]


def compute_portfolio_return(returns: pd.DataFrame, weights_df: pd.DataFrame):
    aligned_cols = list(set(returns.columns).intersection(weights_df.columns))
    R = returns[aligned_cols].copy()
    W = weights_df[aligned_cols].copy()

    # row-wise normalization: divide by the absolute value sum of the weights at the current time
    denom = W.abs().sum(axis=1).replace(0, np.nan)
    W_norm = W.div(denom, axis=0).fillna(0.0)

    port_ret = (R * W_norm).sum(axis=1)
    return port_ret


eig1_ret = compute_portfolio_return(returns, eig1)
eig2_ret = compute_portfolio_return(returns, eig2)

# ---------------------------------------------------------
# BTC & ETH 報酬
# ---------------------------------------------------------
btc_ret = returns["BTC"]
eth_ret = returns["ETH"]


# ---------------------------------------------------------
# Cumulative return
# ---------------------------------------------------------
def cumulative(ret):
    return (1 + ret).cumprod()


cum_eig1 = cumulative(eig1_ret)
cum_eig2 = cumulative(eig2_ret)
cum_btc = cumulative(btc_ret)
cum_eth = cumulative(eth_ret)

# ---------------------------------------------------------
# Plot (Task 1b)
# ---------------------------------------------------------
plt.figure(figsize=(12, 6))
plt.plot(cum_eig1, label="Eigen-Portfolio 1")
plt.plot(cum_eig2, label="Eigen-Portfolio 2")
plt.plot(cum_btc, label="BTC")
plt.plot(cum_eth, label="ETH")

plt.title("Cumulative Return: Eigen-Portfolios vs BTC & ETH")
plt.xlabel("Time")
plt.ylabel("Cumulative Return")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("cumulative_return_4_assets.png")
plt.show()

print("Saved plot: cumulative_return_4_assets.png")


import pandas as pd
import matplotlib.pyplot as plt

# =============================
# Read eigen-portfolio weights
# =============================
eig1 = pd.read_csv(
    "system_design/python_introduction/final_project/results/task1a_1.csv",
    index_col=0,
)
eig2 = pd.read_csv(
    "system_design/python_introduction/final_project/results/task1a_2.csv",
    index_col=0,
)

eig1.index = pd.to_datetime(eig1.index).tz_localize(None)
eig2.index = pd.to_datetime(eig2.index).tz_localize(None)

# =============================
# The two dates (you can change)
# =============================
d1 = pd.Timestamp("2021-10-07")
d2 = pd.Timestamp("2022-04-15")


def plot_eigen_weights(date, eig1, eig2):
    if date not in eig1.index:
        print(f"{date} not found in eigen weights!")
        return

    w1 = eig1.loc[date]
    w2 = eig2.loc[date]

    plt.figure(figsize=(14, 6))
    plt.bar(w1.index, w1.values, label="Eigen-Portfolio 1", alpha=0.7)
    plt.bar(w2.index, w2.values, label="Eigen-Portfolio 2", alpha=0.7)
    plt.xticks(rotation=90)
    plt.title(f"Eigen-Portfolio Weights on {date.date()}")
    plt.ylabel("Weight")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    fname = f"eigen_weights_{date.date()}.png"
    plt.savefig(fname)
    plt.show()
    print(f"Saved: {fname}")


# =============================
# Output two plots
# =============================
plot_eigen_weights(d1, eig1, eig2)
plot_eigen_weights(d2, eig1, eig2)
