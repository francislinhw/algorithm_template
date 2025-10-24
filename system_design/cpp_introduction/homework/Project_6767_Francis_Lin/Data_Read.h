// Data reading header file
#ifndef DATA_READ_H
#define DATA_READ_H

#include <string>
#include <vector>

using namespace std;

struct TotalInterestRateData {
	vector<string> date;
	vector<double> rate;
};

struct TotalStockData {
	vector<string> date;
	vector<double> close_adj;
};

struct TotalOptionData {
	vector<string> date;
	vector<string> exdate;
	vector<string> cp_flag;
	vector<double> strike_price;
	vector<double> best_bid;
	vector<double> best_offer;
};

struct SingleOptionData {
	string date;
	string exdate;
	string cp_flag;
	double strike_price;
	double best_bid;
	double best_offer;
};

void read_interest_data(TotalInterestRateData& total_interest_rate_data);
void read_stock_data(TotalStockData& total_stock_data);
void read_option_data(TotalOptionData& total_option_data);

#endif  // DATA_READ_H