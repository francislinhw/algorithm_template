import pandas as pd
import matplotlib.pyplot as plt

stock_prices = (
    pd.read_csv(
        "/Users/francis/private_projects/algorithm_template/system_design/cpp_introduction/homework/project_one/simulated_stock_prices.csv",
        header=None,
    )
    .iloc[:, :-1]
    .T
)
option_prices = (
    pd.read_csv(
        "/Users/francis/private_projects/algorithm_template/system_design/cpp_introduction/homework/project_one/simulated_option_prices.csv",
        header=None,
    )
    .iloc[:, :-1]
    .T
)
hedging_errors = pd.read_csv(
    "/Users/francis/private_projects/algorithm_template/system_design/cpp_introduction/homework/project_one/cumulative_hedging_errors.csv",
    header=None,
).iloc[:, -2]

# figure 1: 100 Paths of Simulated Stock Price
plt.figure(figsize=(10, 6))
for col in stock_prices.columns[:100]:
    plt.plot(stock_prices[col], alpha=0.6)
plt.title("100 Paths of Simulated Stock Price")
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.savefig("stock_price_paths.png")

# figure 2: 100 Paths of Simulated Option Price
plt.figure(figsize=(10, 6))
for col in option_prices.columns[:100]:
    plt.plot(option_prices[col], alpha=0.6)
plt.title("100 Paths of Simulated Option Price")
plt.xlabel("Time")
plt.ylabel("Option Price")
plt.savefig("option_price_paths.png")

# figure 3: Ditribution of Simulated Hedging Errors
plt.figure(figsize=(10, 6))
plt.hist(hedging_errors.values, bins=20, alpha=0.7)
plt.title("Ditribution of the Cumulative Hedging Errors")
plt.xlabel("Hedging Error")
plt.ylabel("Frequency")
plt.savefig("cumulative_hedging_errors_histogram.png")

plt.show()
