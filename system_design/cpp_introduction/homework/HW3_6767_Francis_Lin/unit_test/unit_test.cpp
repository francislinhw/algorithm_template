#include "../Option_Price.h"
#include <cassert>
#include <iostream>

int main() {
    // Test case 1 for a call option
    Option_Price call_option(100, 105, 0.05, 1, 0.2, 'C');
    
    // Get Black-Scholes and Binomial prices and deltas for call option
    double bs_price_call = call_option.BSM_Pricer();
    double bs_delta_call = call_option.BSM_Delta();
    double binomial_price_call = call_option.Binomial_Pricer();
    double binomial_delta_call = call_option.Binomial_Delta();
    
    // Assert that prices and deltas are greater than 0
    assert(bs_price_call > 0);
    assert(bs_delta_call > 0);
    assert(binomial_price_call > 0);
    assert(binomial_delta_call > 0);
    std::cout << "Test case 1 passed" << std::endl;
    
    // Check if BS and Binomial prices and deltas are consistent (within a tolerance)
    double tolerance = 0.01;
    assert(fabs(bs_price_call - binomial_price_call) < tolerance);  // Prices should be consistent
    assert(fabs(bs_delta_call - binomial_delta_call) < tolerance);  // Deltas should be consistent
    
    std::cout << "Test case 2: BS and Binomial pricing and delta tests passed!" << std::endl;
    
    // Test for a put option
    Option_Price put_option(100, 95, 0.05, 1, 0.2, 'P');
    
    // Get Black-Scholes and Binomial prices and deltas for put option
    double bs_price_put = put_option.BSM_Pricer();
    double bs_delta_put = put_option.BSM_Delta();
    double binomial_price_put = put_option.Binomial_Pricer();
    double binomial_delta_put = put_option.Binomial_Delta();

    std::cout << "Test case 3 passed: Put option" << std::endl;
    // Assert that prices and deltas are greater than 0 (or in case of delta, less than 0 for puts)
    assert(bs_price_put > 0);
    assert(bs_delta_put < 0);
    assert(binomial_price_put > 0);
    assert(binomial_delta_put < 0);
    std::cout << "Test case 4 passed: Put option" << std::endl;
    
    // Check if BS and Binomial prices and deltas are consistent (within a tolerance)
    assert(fabs(bs_price_put - binomial_price_put) < tolerance);  // Prices should be consistent
    assert(fabs(bs_delta_put - binomial_delta_put) < tolerance);  // Deltas should be consistent
    
    std::cout << "Test case 5: Consistency test passed!" << std::endl;

    std::cout << "All tests passed!" << std::endl;

    return 0;
}
