#include "Option_Price.h"
#include <cmath>
#include <vector>
#include <algorithm>

// Constructor
Option_Price::Option_Price(double strike, double underlyingPrice, double riskFreeRate, double timeToMaturity, double volatility, char optionType)
    : Option(strike, underlyingPrice, riskFreeRate, timeToMaturity, volatility), flag(optionType) {}

// Helper function to calculate the standard normal cumulative distribution function (CDF)
double norm_cdf(double x) {
    return 0.5 * std::erfc(-x * M_SQRT1_2);  // M_SQRT1_2 is 1/sqrt(2)
}

// Black-Scholes Pricer
double Option_Price::BSM_Pricer() const {
    // Calculate d1 and d2 using Black-Scholes formula
    double d1 = (log(getS() / getK()) + (getR() + 0.5 * getSigma() * getSigma()) * getT()) / (getSigma() * sqrt(getT()));
    double d2 = d1 - getSigma() * sqrt(getT());

    if (flag == 'C' || flag == 'c') {
        // Call option price
        return getS() * norm_cdf(d1) - getK() * exp(-getR() * getT()) * norm_cdf(d2);
    } else {
        // Put option price
        return getK() * exp(-getR() * getT()) * norm_cdf(-d2) - getS() * norm_cdf(-d1);
    }
}

// Black-Scholes Delta calculation
double Option_Price::BSM_Delta() const {
    double d1 = (log(getS() / getK()) + (getR() + 0.5 * getSigma() * getSigma()) * getT()) / (getSigma() * sqrt(getT()));
    
    if (flag == 'C' || flag == 'c') {
        // Call option Delta: N(d1)
        return norm_cdf(d1);
    } else {
        // Put option Delta: N(d1) - 1
        return norm_cdf(d1) - 1;
    }
}

// Binomial Pricer using the Binomial Lattice Method
double Option_Price::Binomial_Pricer() const {
    const int N = 1000;  // Number of steps in the binomial tree
    double dt = getT() / N;  // Time step size
    double u = exp(getSigma() * sqrt(dt));  // Up factor
    double d = 1 / u;  // Down factor
    double p = (exp(getR() * dt) - d) / (u - d);  // Risk-neutral probability

    // Step 1: Create a price tree
    std::vector<double> price(N + 1);
    for (int i = 0; i <= N; ++i) {
        price[i] = getS() * pow(u, N - i) * pow(d, i);  // Stock prices at maturity
    }

    // Step 2: Create the option value tree at maturity
    std::vector<double> option_value(N + 1);
    for (int i = 0; i <= N; ++i) {
        if (flag == 'C' || flag == 'c') {
            // Call option payoff
            option_value[i] = std::max(0.0, price[i] - getK());
        } else {
            // Put option payoff
            option_value[i] = std::max(0.0, getK() - price[i]);
        }
    }

    // Step 3: Backward induction to get the option price at time 0
    for (int step = N - 1; step >= 0; --step) {
        for (int i = 0; i <= step; ++i) {
            option_value[i] = (p * option_value[i] + (1 - p) * option_value[i + 1]) * exp(-getR() * dt);
        }
    }

    // The option price at the root (time 0)
    return option_value[0];
}

// Binomial Delta using full Binomial Lattice Method with backtracking
double Option_Price::Binomial_Delta() const {
    const int N = 1000;  // Number of steps in the binomial tree
    double dt = getT() / N;  // Time step size
    double u = exp(getSigma() * sqrt(dt));  // Up factor
    double d = 1 / u;  // Down factor
    double p = (exp(getR() * dt) - d) / (u - d);  // Risk-neutral probability

    // Step 1: Create a price tree
    std::vector<std::vector<double>> stock_price(N + 1, std::vector<double>(N + 1));
    for (int i = 0; i <= N; ++i) {
        for (int j = 0; j <= i; ++j) {
            stock_price[i][j] = getS() * pow(u, j) * pow(d, i - j);  // Calculate stock price at node (i, j)
        }
    }

    // Step 2: Create an option value tree at maturity
    std::vector<std::vector<double>> option_value(N + 1, std::vector<double>(N + 1));
    for (int j = 0; j <= N; ++j) {
        if (flag == 'C' || flag == 'c') {
            // Call option payoff at maturity
            option_value[N][j] = std::max(0.0, stock_price[N][j] - getK());
        } else {
            // Put option payoff at maturity
            option_value[N][j] = std::max(0.0, getK() - stock_price[N][j]);
        }
    }

    // Step 3: Backward induction to calculate option value at earlier steps
    for (int i = N - 1; i >= 0; --i) {
        for (int j = 0; j <= i; ++j) {
            option_value[i][j] = (p * option_value[i + 1][j + 1] + (1 - p) * option_value[i + 1][j]) * exp(-getR() * dt);
        }
    }

    // Step 4: Calculate Delta at the first step
    double delta = (option_value[1][1] - option_value[1][0]) / (stock_price[1][1] - stock_price[1][0]);

    return delta;
}