import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# Black-Scholes exact solution for a European call option
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def crank_nicholson_sor(
    S_max, K, T, sigma, r, M, N, omega=1.3, tol=1e-10, max_iter=10000
):
    """
    Solve the Black-Scholes equation using Crank-Nicholson with Successive Over-Relaxation (SOR).
    """

    dS = S_max / M
    dt = T / N
    S = np.linspace(0, S_max, M + 1)
    V = np.maximum(S - K, 0)  # Terminal condition for European Call

    # Coefficients
    alpha = 0.25 * dt * (sigma**2 * (S / dS) ** 2 - r * S / dS)
    beta = -0.5 * dt * (sigma**2 * (S / dS) ** 2 + r)
    gamma = 0.25 * dt * (sigma**2 * (S / dS) ** 2 + r * S / dS)

    # Time-stepping loop (starting from maturity, moving backward)
    for n in range(N - 1, -1, -1):
        V[-1] = S_max - K * np.exp(-r * (T - n * dt))
        error = np.inf
        iteration = 0
        V_old = V.copy()  # Copy the entire array to track changes

        while error > tol and iteration < max_iter:
            error = 0.0
            for j in range(1, M):  # Fix upper bound (previously caused index error)
                # Compute intermediate y using Crank-Nicholson equation
                y = (V_old[j] + alpha[j] * V[j - 1] + gamma[j] * V[j + 1]) / (1 - beta[j])

                # Apply SOR update
                new_V = max(
                    V[j] + omega * (y - V[j]), 0
                )  # Ensure non-negative option price

                # Compute error for convergence
                error += (new_V - V[j]) ** 2
                V[j] = new_V  # Update value and discount

            error = np.sqrt(error)
            iteration += 1

        # Debugging output to check changes
        print(f"Time step {n}, Iterations: {iteration}, Error: {error}")

    return S, V


omega = 1.1  # Relaxation factor


# Parameters
S_max = 150  # Maximum stock price
K = 50  # Strike price
T = 1  # Time to maturity
sigma = 0.2  # Volatility
r = 0.05  # Risk-free rate
M = 300  # Number of space steps
N = 1000  # Number of time steps

# Run Crank-Nicolson method
# Solve using Crank-Nicholson with SOR
S, V_numerical = crank_nicholson_sor(S_max, K, T, sigma, r, M, N, omega)

# Compute exact Black-Scholes prices
V_exact = black_scholes_call(S, K, T, r, sigma)

# Compute absolute error
error = np.abs(V_numerical - V_exact)

# Display Error as chart
plt.figure(figsize=(10, 6))
plt.plot(S, error, label="Error", color="blue")
plt.title("Error of Numerical Solution")
plt.show()

# Display results
import pandas as pd


df = pd.DataFrame(
    {
        "Stock Price S": S,
        "Numerical Price": V_numerical,
        "Black-Scholes Price": V_exact,
        "Absolute Error": error,
    }
)

print(df)


# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(S, V_numerical, label="Numerical Solution", color="blue")
plt.plot(S, V_exact, label="Black-Scholes Solution", color="red")
plt.title("European Call Option Pricing")
plt.legend(loc="upper left")
plt.xlabel("Stock Price S")
plt.ylabel("Option Price")
plt.show()
