// Simulation program file
#include "Simulation.h"
#include "Option_Price.h"
#include "utils.h"
#include <vector>
#include <fstream>
#include <iostream>
#include <cmath>
#include <random>

using namespace std;

// Function to run the simulation
void simulationFun(
    int simulation_num, double S_0, double T, double mu, double sigma, double r, double N, double K
)
{
    double dt = T / N;
    double hedging_error;

    // ✅ 改成 N+1，因為要存 0~N 共 N+1 個點
    vector<double> stock_price(N + 1), option_price(N + 1), delta(N + 1), b(N + 1);

    // Initialize the first stock price, option price, delta, and b
    Option_Price simu_option(K, S_0, r, T, sigma, 'C');
    auto pricer = simu_option.BSM_Pricer();
    option_price[0] = pricer.first;
    delta[0] = pricer.second;
    b[0] = option_price[0] - delta[0] * S_0;
    stock_price[0] = S_0;

    ofstream stock_price_path("simulated_stock_prices.csv");
    ofstream option_price_path("simulated_option_prices.csv");
    ofstream hedging_error_csv("cumulative_hedging_errors.csv");

    for (int i = 0; i < simulation_num; ++i) {
        stock_price_path << S_0 << ",";
        option_price_path << option_price[0] << ",";

        for (int j = 1; j <= N; ++j) { // ✅ 這裡合法，因為 vector 長度是 N+1
            // Simulate the stock prices
            double rnd = randomGenerate(1000 * i + j);
            stock_price[j] = (
                stock_price[j - 1] +
                mu * stock_price[j - 1] * dt +
                sigma * stock_price[j - 1] * sqrt(dt) * rnd
            );
            stock_price_path << stock_price[j] << ",";

            // Update option data
            simu_option.S = stock_price[j];
            simu_option.T = T - j * dt;
            pricer = simu_option.BSM_Pricer();
            option_price[j] = pricer.first;
            delta[j] = pricer.second;
            option_price_path << option_price[j] << ",";

            // Calculate the hedging errors
            b[j] = (
                delta[j - 1] * stock_price[j] + b[j - 1] * exp(r * dt) - delta[j] * stock_price[j]
            );
            hedging_error = (
                delta[j - 1] * stock_price[j] + b[j - 1] * exp(r * dt) - option_price[j]
            );
            hedging_error_csv << hedging_error << ",";
        }

        stock_price_path << endl;
        option_price_path << endl;
        hedging_error_csv << endl;
    }

    stock_price_path.close();
    option_price_path.close();
    hedging_error_csv.close();
}
