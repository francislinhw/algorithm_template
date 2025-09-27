#ifndef OPTION_PRICE_H
#define OPTION_PRICE_H

#include "Option.h"
#include "Pricing_Method.h"

class Option_Price : public Option, public Pricing_Method {
public:
    char flag;  // 'C' for Call, 'P' for Put

    // Constructor with parameters
    Option_Price(double strike, double underlyingPrice, double riskFreeRate, double timeToMaturity, double volatility, char optionType);

    // Implement Black-Scholes Pricer and Delta
    double BSM_Pricer() const override;
    double BSM_Delta() const override;

    // Implement Binomial Pricer and Delta
    double Binomial_Pricer() const override;
    double Binomial_Delta() const override;
};

#endif // OPTION_PRICE_H