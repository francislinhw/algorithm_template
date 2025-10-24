// Main program file
#include "Simulation.h"
#include "Data_Read.h"
#include "PNL_Cal.h"
#include "test.h"

using namespace std;

int main() {
	// Task 1
	int simulation_num;
	double S_0, T, mu, sigma, r, N, K;

	simulationFun(simulation_num=1000, S_0=100, T=0.4, mu=0.05, sigma=0.24, r=0.025, N=100, K=105);

	// Task 2
	// Unit test for calculating implied volatility and a unit test for calculating delta
	testCases();

	// Main program
	TotalInterestRateData total_interest_rate_data;
    TotalStockData total_stock_data;
    TotalOptionData total_option_data;

    read_stock_data(total_stock_data);
    read_option_data(total_option_data);
    read_interest_data(total_interest_rate_data);

    deltaHedgingPortfolioConstruct(
		"2011-07-05", "2011-07-29", "2011-09-17", "C", 
		500, total_interest_rate_data, total_stock_data, total_option_data
	);
    
	system("pause");
    return 0;
}