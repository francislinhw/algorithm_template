// Utility functions header file
#ifndef HELPER_FUNC_H
#define HELPER_FUNC_H

#include <string>
#include "Data_Read.h"
#include "Option_Price.h"

// Calculate the standard normal CDF
double normCdf(double x);

// Generate random numbers
double randomGenerate(int seed);

// Given a date, get the index of previous date
int getPreviousDateIndex(const vector<string>& dates, const string& target_date);

// Number of date count
int dateCount(
    const std::string& start_date, const std::string& end_date, 
    const TotalInterestRateData& interest_rate_data
);

// Search option price in the option data
double optionPriceSearch(
    TotalOptionData option_data, string current_date, string exp_date, string flag, double strike
);

// Binary search for implied volatility
double volBinarySearch(Option_Price option, double target_price, double low, double high);

#endif  // HELPER_FUNC_H