#include "Data_Read.h"
#include <fstream>
#include <sstream>
#include <string>

void read_interest_data(TotalInterestRateData& total_interest_rate_data) {
    // Read the interest rate data from the file
    std::string single_line, temp_data;
    std::ifstream rate_infile("interest.csv");
    getline(rate_infile, single_line); // Skip first row(header of the file)

    // Read the data from the file until the end
    while (getline(rate_infile, single_line)) {
        std::istringstream istream(single_line);

        // Read the date data
        getline(istream, temp_data, ',');
        total_interest_rate_data.date.push_back(temp_data);

        // Read the interest rate data
        getline(istream, temp_data, ',');
        total_interest_rate_data.rate.push_back(std::stod(temp_data));
    }
}

void read_stock_data(TotalStockData& total_stock_data) {
    // Read the stock price data from the file
    std::string single_line, temp_data;
    std::ifstream stock_infile("sec_GOOG.csv");
    getline(stock_infile, single_line); //Skip first row(header of the file)

    // Read the data from the file until the end
    while (getline(stock_infile, single_line)) {
        std::istringstream istream(single_line);

        // Read the date data
        getline(istream, temp_data, ',');
        total_stock_data.date.push_back(temp_data);

        // Read the adjusted close price data
        getline(istream, temp_data, ',');
        total_stock_data.close_adj.push_back(std::stod(temp_data));
    }
}

void read_option_data(TotalOptionData& total_option_data) {
    // Read the option data from the file
    std::string single_line, temp_data;
    std::ifstream option_infile("op_GOOG.csv");
    getline(option_infile, single_line); //Skip first row(header of the file)

    // Read the data from the file until the end
    while (getline(option_infile, single_line)) {
        std::istringstream istream(single_line);

        // Read the date data
        getline(istream, temp_data, ',');
        total_option_data.date.push_back(temp_data);

        // Read the execution date data
        getline(istream, temp_data, ',');
        total_option_data.exdate.push_back(temp_data);

        // Read the call/put flag data
        getline(istream, temp_data, ',');
        total_option_data.cp_flag.push_back(temp_data);

        // Read the strike price data
        getline(istream, temp_data, ',');
        total_option_data.strike_price.push_back(std::stod(temp_data));

        // Read the best bid data
        getline(istream, temp_data, ',');
        total_option_data.best_bid.push_back(std::stod(temp_data));

        // Read the best offer data
        getline(istream, temp_data, ',');
        total_option_data.best_offer.push_back(std::stod(temp_data));
    }
}