// PNL calculation header file
#ifndef PNL_CAL_H
#define PNL_CAL_H

#include <string>
#include "Data_Read.h"

void deltaHedgingPortfolioConstruct(
    const std::string& t_0,
	const std::string& t_N,
    const std::string& exp_date,
    const std::string& flag,
    double strike_price,
    const TotalInterestRateData& interest_rate_data,
    const TotalStockData& stock_data,
    const TotalOptionData& option_data
);

#endif  // PNL_CAL_H