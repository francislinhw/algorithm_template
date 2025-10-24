#include <cmath>
#include <random>
#include <string>
#include "Data_Read.h"
#include <algorithm>
#include <iostream>
#include "Option_Price.h"

// Calculate the standard normal CDF
double normCdf(double x) {
    return 0.5 * std::erfc(-x / sqrt(2.0));  // M_SQRT1_2 = 1/sqrt(2)
}

// Generate random numbers
double randomGenerate(int seed) {
	std::default_random_engine gen(seed);
	std::normal_distribution<double> n(0, 1);
	return n(gen);
}

// Given a date, get the index of previous date
int getPreviousDateIndex(const vector<string>& dates, const string& target_date) {
    auto it = std::lower_bound(dates.begin(), dates.end(), target_date);
    
    // if target_date is smaller than the smallest date in dates vector, return -1
    if (it == dates.begin()) {
        return -1;
    }
    
    // if can not find date that exactly match, return the index of previous date
    if (it == dates.end() || *it != target_date) {
        --it;  // find the previous date
    }
    
    return std::distance(dates.begin(), it);
}

// Number of date count
int dateCount(
    const std::string& start_date, 
    const std::string& end_date, 
    const TotalInterestRateData& interest_rate_data
)
{
    int index1 = getPreviousDateIndex(interest_rate_data.date, start_date);
    int index2 = getPreviousDateIndex(interest_rate_data.date, end_date);

    if (index1 == -1 || index2 == -1) {
        std::cerr << "❌ dateCount(): Date not found in interest_rate_data. start_date=" 
                  << start_date << " end_date=" << end_date << std::endl;
        return 0; // 不要回 -1，避免 vector 爆掉
    }

    int index_diff = abs(index2 - index1) + 1;

    // 額外安全檢查：如果 index_diff 超大或不合理
    if (index_diff > (int)interest_rate_data.date.size()) {
        std::cerr << "⚠️ dateCount(): Computed diff too large, clipping to max size." << std::endl;
        index_diff = interest_rate_data.date.size();
    }

    return index_diff;
}

// Search option price in the option data
double optionPriceSearch(
    TotalOptionData option_data, string current_date, string exp_date, string flag, double strike
) {
	for (size_t i = 0; i < option_data.date.size(); i++) {
		
		if (
            (option_data.date[i] == current_date) & 
            (option_data.exdate[i] == exp_date) & 
            (option_data.cp_flag[i] == flag) & 
            (option_data.strike_price[i] == strike)
        ) {
			
			return (option_data.best_bid[i] + option_data.best_offer[i]) / 2;

		}
		
	}
	return 0;
}

// Binary search for implied volatility
double volBinarySearch(Option_Price option, double target_price, double low, double high) {
	double tolerance = 0.00001;

	Option_Price high_option = option;
	Option_Price low_option = option;
	high_option.sigma = high;
	low_option.sigma = low;

    // If the interval is invalid, return 0
	if (low > high) {
		cout << "Invalid interval input" << endl;
		return 0;
	}

    // If the target price is out of the interval, return 0
	else if ((
        (high_option.BSM_Pricer().first - target_price) * (low_option.BSM_Pricer().first - target_price)
    ) > 0) 
    {
		cout << "Invalid target price input" << endl;
        return 0;
	}

	else {
        do {
            if (option.BSM_Pricer().first > target_price) {
                high = option.sigma;
            }
            if (option.BSM_Pricer().first < target_price) {
                low = option.sigma;
            }
            option.sigma = (low + high) / 2;

        } while (fabs(option.BSM_Pricer().first - target_price) > tolerance);

        return option.sigma;
		}
}
