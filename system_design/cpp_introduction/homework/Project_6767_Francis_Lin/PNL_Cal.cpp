#include "PNL_Cal.h"
#include "Option_Price.h"
#include "Data_Read.h"
#include "utils.h"
#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <cmath>


void deltaHedgingPortfolioConstruct(
    const std::string& t_0,
	const std::string& t_N,
    const std::string& exp_date,
    const std::string& flag,
    double strike_price,
    const TotalInterestRateData& interest_rate_data,
    const TotalStockData& stock_data,
    const TotalOptionData& option_data
)
{
    int date_num_testing_period = dateCount(t_0, t_N, interest_rate_data);
    int date_num_total = dateCount(t_0, exp_date, interest_rate_data);
	
    // Initialize variables
    double current_stock_price, current_interest_rate, current_option_price;
	double original_option_price, maturity, PNL, hedging_error;
    double low = 0.0, high = 1.0; // Upper and lower bounds for implied volatility
    std::string current_date;
    std::vector<double> B(date_num_testing_period), delta(date_num_testing_period);

    // Locate the starting indices for stock and rate data
    int stock_starting_idx = getPreviousDateIndex(stock_data.date, t_0);
    int intereset_rate_starting_idx = getPreviousDateIndex(interest_rate_data.date, t_0);

    std::ofstream result_csv;
    result_csv.open("result.csv");
    result_csv << "date,S,V,Implied volatility,delta,HE,PNL,PNL (with hedge)" << std::endl;

    // Calculate delta hedging portfolio
	for (int i = 0; i < date_num_testing_period; ++i) {
		// Get current data
		current_date = stock_data.date[stock_starting_idx + i];
		current_stock_price = stock_data.close_adj[stock_starting_idx + i];
		current_interest_rate = interest_rate_data.rate[intereset_rate_starting_idx + i]/100.0;
		current_option_price = optionPriceSearch(option_data, current_date, exp_date, flag, strike_price);
		maturity = (date_num_total - i) / 252.0;

		if (i == 0) {
			original_option_price = current_option_price;
		}

		Option_Price current_option(
            strike_price, current_stock_price, current_interest_rate, 
			maturity, (high + low) / 2, flag.c_str()[0]
        );

		// Search for implied volatility
		current_option.sigma = volBinarySearch(current_option, current_option_price, low, high);

		// Calculate delta
		delta[i] = current_option.BSM_Pricer().second;

		// Calculate hedging error
		if (i == 0) {
			B[i] = current_option_price - delta[i] * current_stock_price;
			hedging_error = 0;
		}
		else {
			B[i] = (
				(delta[i - 1] * current_stock_price + 
				B[i - 1] * exp(interest_rate_data.rate[intereset_rate_starting_idx + i - 1] / 25200)) 
				- delta[i] * current_stock_price
			);
			hedging_error = (
				(delta[i - 1] * current_stock_price + 
				B[i - 1] * exp(interest_rate_data.rate[intereset_rate_starting_idx + i - 1] / 25200))
				 - current_option_price
			);
		}

		// Calculate PNL
		PNL = original_option_price - current_option_price;

		// Write the result to the csv file
		result_csv << current_date << "," << current_stock_price << "," << current_option_price << ","
		<< current_option.sigma << "," << delta[i] << ","
		<< hedging_error << "," << PNL << "," << hedging_error << std::endl;
	}

	result_csv.close();
}