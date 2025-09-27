#include <iostream>
#include "Option_Price.h"

int main() {

    // User input
    double K, S, r, T, sigma;
    char optionType;
    
    while (true) {
        std::cout << "Enter Strike Price (K): ";
        std::cin >> K;
        std::cout << "Enter Underlying Price (S): ";
        std::cin >> S;
        std::cout << "Enter Risk-free Rate (r): ";
        std::cin >> r;
        std::cout << "Enter Time to Maturity (T): ";
        std::cin >> T;
        std::cout << "Enter Volatility (σ): ";
        std::cin >> sigma;
        std::cout << "Enter Option Type (C for Call, P for Put): ";
        std::cin >> optionType;

        // Create an Option_Price object
        Option_Price option(K, S, r, T, sigma, optionType);

        // Output results
        std::cout << "Black-Scholes Price: " << option.BSM_Pricer() << std::endl;
        std::cout << "Black-Scholes Delta: " << option.BSM_Delta() << std::endl;
        std::cout << "Binomial Price: " << option.Binomial_Pricer() << std::endl;
        std::cout << "Binomial Delta: " << option.Binomial_Delta() << std::endl;
    
        std::cout << "Enter 1 to continue, 0 to exit: ";
        int continueInput;
        std::cin >> continueInput;
        if (continueInput == 0) {
            break;
        }
    }

    return 0;
}