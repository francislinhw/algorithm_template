// Unit test header file for task 2
#ifndef UNIT_TEST_H
#define UNIT_TEST_H

#include "Option_Price.h"
#include "utils.h"
#include <iostream>
#include <cmath>


int testFun(
    double K, double S, double r, double T, double option_price, char option_type, 
    double target_sigma, double target_delta
) {
    double low = 0.0, high = 1.0, tolerance = 0.001;
    Option_Price option_for_vol_search(K, S, r, T, (high + low) / 2, option_type);
    // Search for implied volatility
    double searched_sigma = volBinarySearch(option_for_vol_search, option_price, low, high);
    cout << "Searched implied volatility: " << searched_sigma << endl;
    cout << "Target implied volatility: " << target_sigma << endl;

    // Calculate delta
    Option_Price option_for_delta_cal(K, S, r, T, target_sigma, option_type);
    double calculated_delta = option_for_delta_cal.BSM_Pricer().second;
    cout << "Calculated delta: " << calculated_delta << endl;
    cout << "Target delta: " << target_delta << endl;

    if (
        fabs(searched_sigma - target_sigma) < tolerance && fabs(calculated_delta - target_delta) < tolerance
    ) {
        std::cout << "Test passed!" << std::endl;
        return 0;
    } else {
        std::cout << "Test failed!" << std::endl;
        return 1;
    }
}

void testCases() {
    std::cout << "Running test cases of task 2..." << std::endl;

    int count = 0;
    count += testFun(100, 105, 0.06, 15, 66.907, 'C', 0.2, 0.946539);
    count += testFun(100, 95, 0.10, 11, 2.15634, 'P', 0.25, -0.0465404);
    if (count == 0) {
        std::cout << "All test cases passed!" << std::endl;
    } else {
        std::cout << "Some test cases failed!" << std::endl;
    }
    std::cout << std::endl;
}

#endif // TEST1_H_INCLUDED

