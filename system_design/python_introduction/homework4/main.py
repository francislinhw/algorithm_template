import numpy as np
import numpy.typing as npt
import pandas as pd
import matplotlib.pyplot as plt
import os

# guarantee the path is relative to this file
BASE_DIR = os.path.dirname(__file__)
AAPL_CSV_PATH = os.path.join(BASE_DIR, "aapl.csv")


"""
Task 1
"""
print("Task 1:\n")


def trading_strategy(
    csv_file_name: str,
) -> tuple[npt.NDArray[np.int_], npt.NDArray[np.int_], npt.NDArray[np.float_]]:
    """
    A simple trading strategy:
    - Buy 10 shares after 3 consecutive price increases (up to 20 shares max)
    - Sell all shares after 2 consecutive price decreases
    - Always liquidate remaining shares on the last day
    """
    # --- Load data ---
    raw_data = pd.read_csv(csv_file_name)
    dates = raw_data["Date"].values
    prices = raw_data["Adj Close"].values

    n = len(prices)
    sh = 10
    w = 10000
    curr_sh = 0
    consecutive_increase = 0
    consecutive_decrease = 0

    if n == 0:
        return np.zeros(1, dtype=int), np.zeros(1, dtype=int), np.zeros(1, dtype=float)

    signals = np.zeros(n, dtype=int)
    positions = np.zeros(n, dtype=int)
    account_value = np.full(n, w, dtype=float)

    for i in range(1, n - 1):

        if prices[i] > prices[i - 1]:
            consecutive_increase += 1
            consecutive_decrease = 0

            if consecutive_increase == 3 and curr_sh < 2 * sh:
                signals[i] = 1
                curr_sh += sh
                w -= sh * prices[i]
                consecutive_increase = 2

        elif prices[i] < prices[i - 1]:
            consecutive_decrease += 1
            consecutive_increase = 0

            if consecutive_decrease == 2 and curr_sh > 0:
                signals[i] = -1
                w += curr_sh * prices[i]
                curr_sh = 0
                consecutive_decrease = 1

        else:
            consecutive_increase = 0
            consecutive_decrease = 0

        positions[i] = curr_sh
        account_value[i] = w + curr_sh * prices[i]

    if curr_sh > 0:
        signals[-1] = -1
        w += curr_sh * prices[-1]
        curr_sh = 0
    else:
        signals[-1] = 0

    account_value[-1] = w

    print(f"Final Cumulative P&L: {account_value[-1] - 10000}")

    # --- Save results ---
    trading_results = pd.DataFrame(
        {
            "Dates": dates,
            "Signals": signals,
            "Positions": positions,
            "Account Value": account_value,
        }
    )
    trading_results.to_csv("trading_results.csv", index=False)

    return signals, positions, account_value


# --- Task 1 unit test ---
print("Task 1 unit test:")
test_prices = [0, 1, 2, 3]
test_dates = [str(i) for i in range(1, len(test_prices) + 1)]
test_df = pd.DataFrame({"Date": test_dates, "Adj Close": test_prices})
test_df.to_csv("test_price.csv", index=False)

expected_signals = np.array([0, 0, 0, 0])
expected_positions = np.array([0, 0, 0, 0])
expected_account_value = np.array([10000, 10000, 10000, 10000])

test_signals, test_positions, test_account_value = trading_strategy("test_price.csv")

if (
    np.array_equal(test_signals, expected_signals)
    and np.array_equal(test_positions, expected_positions)
    and np.array_equal(test_account_value, expected_account_value)
):
    print("Task 1 unit test passed.")
else:
    print("Task 1 unit test failed.")

# --- Example Case ---
print("\nExample Case:")
example_prices = [98, 100, 102, 104, 103, 101, 99, 100, 102, 104, 106, 107, 105]
example_dates = [str(i) for i in range(1, len(example_prices) + 1)]
example_df = pd.DataFrame({"Date": example_dates, "Adj Close": example_prices})
example_df.to_csv("example_price.csv", index=False)
example_signals, example_positions, example_account_value = trading_strategy(
    "example_price.csv"
)
print(pd.read_csv("trading_results.csv"))

# --- AAPL Case ---
print("\nAAPL Case:")
final_signals, final_positions, final_account_value = trading_strategy(AAPL_CSV_PATH)
trading_df = pd.read_csv("trading_results.csv")
print(trading_df)

# --- Plot 1: cumulative P&L ---
time_labels = pd.read_csv(AAPL_CSV_PATH)["Date"]
plt.figure(figsize=(10, 5))
plt.plot(time_labels, final_account_value - 10000, label="Cumulative P&L", lw=1.5)
plt.title("Cumulative P&L figure")
plt.xlabel("Date")
plt.ylabel("Cumulative P&L")
plt.xticks(
    [i for i in range(0, len(time_labels), int(len(time_labels) / 5))],
    [time_labels[i] for i in range(0, len(time_labels), int(len(time_labels) / 5))],
)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("Cumulative_P&L.png")
# --- Plot 2: price + buy/sell signals ---
adj_close = pd.read_csv(AAPL_CSV_PATH)["Adj Close"].values
buy_idx = np.where(final_signals == 1)[0]
sell_idx = np.where(final_signals == -1)[0]

plt.figure(figsize=(10, 5))
plt.plot(time_labels, adj_close, label="Adj Close", lw=1)
plt.scatter(
    buy_idx,
    adj_close[buy_idx],
    color="green",
    label="Buy Signal ▲",
    marker="^",
    s=80,
)
plt.scatter(
    sell_idx,
    adj_close[sell_idx],
    color="red",
    label="Sell Signal ▼",
    marker="v",
    s=80,
)
plt.title("AAPL Price with Trading Signals")
plt.xlabel("Index")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("Trading_Signals.png")
plt.show()


"""
Task 2
"""
print("\n-------------------------------------------------------\n")


def min_initial_energy(maze: npt.NDArray[np.int_]) -> int:
    """
    Compute the minimum initial energy required to reach the bottom-right corner.
    The traveler must always maintain energy >= 1.
    """
    m, n = maze.shape
    print("Maze:")
    print(maze)

    dp = np.full((m + 1, n + 1), np.inf)
    dp[m][n - 1] = dp[m - 1][n] = 0

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            need = min(dp[i + 1][j], dp[i][j + 1]) - maze[i][j]
            dp[i][j] = need if need + maze[i][j] >= 1 else -maze[i][j] + 1

    print("Energy required at each cell:")
    print(dp[:m, :n])

    # --- Visualization: Maze energy map ---
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].imshow(maze, cmap="coolwarm", interpolation="nearest")
    axes[0].set_title("Maze Energy Map (Input)")
    for i in range(m):
        for j in range(n):
            axes[0].text(j, i, maze[i, j], ha="center", va="center", color="black")

    axes[1].imshow(dp[:m, :n], cmap="YlGn", interpolation="nearest")
    axes[1].set_title("Min Initial Energy Needed per Cell")
    for i in range(m):
        for j in range(n):
            axes[1].text(j, i, int(dp[i, j]), ha="center", va="center", color="black")

    plt.tight_layout()
    plt.savefig("Maze_Energy_Map.png")
    # plt.show()

    return int(dp[0][0])


# --- Task 2 Unit Test ---
print("Task 2 unit test:")
test_maze = np.array([[-1, -2], [1, 2]])
test_initial_energy = min_initial_energy(test_maze)
if test_initial_energy == 2:
    print("Task 2 unit test passed.")
else:
    print("Task 2 unit test failed.")

# --- Example Case ---
print("\nExample Case:")
example_maze = np.array([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
example_initial_energy = min_initial_energy(example_maze)
print(f"Minimum initial energy required by the example: {example_initial_energy}")

# --- Arbitrary Case ---
print("\nArbitrary Case:")
arbitrary_maze = np.array([[-2, -3, -1], [1, -1, 1], [1, 1, 1]])
arbitrary_initial_energy = min_initial_energy(arbitrary_maze)
print(f"Minimum initial energy required by arbitrary maze: {arbitrary_initial_energy}")
