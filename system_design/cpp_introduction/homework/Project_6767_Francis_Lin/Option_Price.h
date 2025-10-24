// Option price and calculation header file
#ifndef OPTION_PRICE_H
#define OPTION_PRICE_H

#include <utility>

class Option {
private:
    void init();  // Private method to initialize the option class with default parameters

public:

    double K;      // Strike price
    double S;      // Current price of underlying
    double r;      // Risk free rate
    double T;      // Time to maturity
    double sigma;  // Volatility

    // A default constructor
    Option();

    // A constructor with all parameters as arguments to initialize 
    // the option with different given parameter values
    Option(
        double strikePrice, double underlyingPrice, double riskFreeRate, 
        double timeToMaturity, double volatility
    );

    // A destructor
    ~Option();

    // Get method for each of the parameters
    double getStrikePrice() const;
    double getUnderlyingPrice() const;
    double getRiskFreeRate() const;
    double getTimeToMaturity() const;
    double getVolatility() const;
};  

class Pricing_Method {
public:
    // Pure virtual function to calculate the European option price and Delta value
    // using Black-Scholes-Merton’s analytical pricing formula
    virtual std::pair<double, double> BSM_Pricer() const = 0;
};

class Option_Price : public Option, public Pricing_Method {
public:
    char optType;  // 'C' for Call, 'P' for Put

    // Constructor
    Option_Price(
        double strike, double underlyingPrice, double riskFreeRate, 
        double timeToMaturity, double volatility, char optionType
    );

    // Implement Black-Scholes-Merton’s Pricer and Delta Calculator
    std::pair<double, double> BSM_Pricer() const override;

};

#endif // OPTION_PRICE_H