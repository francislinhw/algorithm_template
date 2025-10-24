// Option price and calculation file
#include "Option_Price.h"
#include "utils.h"
#include <cmath>

// Initialize default parameters
void Option::init() {
    K = 100.0;
    S = 100.0;
    r = 0.05;
    T = 1.0;
    sigma = 0.1;
}

// Default constructor
Option::Option() { init(); }

// Constructor with all parameters as arguments to initialize 
// the option with different given parameter values
Option::Option(
    double strikePrice, double underlyingPrice, double riskFreeRate, 
    double timeToMaturity, double volatility
) 
    : K(strikePrice), S(underlyingPrice), r(riskFreeRate), T(timeToMaturity), sigma(volatility) {}

// Destructor
Option::~Option() {}

// Get method for each of the parameters
double Option::getStrikePrice() const { return K; }
double Option::getUnderlyingPrice() const { return S; }
double Option::getRiskFreeRate() const { return r; }
double Option::getTimeToMaturity() const { return T; }
double Option::getVolatility() const { return sigma; } 

// Constructor
Option_Price::Option_Price(
    double strike, double underlyingPrice, double riskFreeRate, 
    double timeToMaturity, double volatility, char optionType
)
    : Option(strike, underlyingPrice, riskFreeRate, timeToMaturity, volatility), optType(optionType) {}

// Black-Scholes-Merton’s Pricer
std::pair<double, double> Option_Price::BSM_Pricer() const {
    // Calculate d1 and d2
    double d1 = (
        log(getUnderlyingPrice() / getStrikePrice()) 
        + 
        (getRiskFreeRate() + 0.5 * pow(getVolatility(), 2)) * getTimeToMaturity()
    ) / (
        getVolatility() * sqrt(getTimeToMaturity())
    );
    double d2 = d1 - getVolatility() * sqrt(getTimeToMaturity());

    double price;
    double delta;
    if (optType == 'C' || optType == 'c') {
        // Call option price
        price = (
            getUnderlyingPrice() * normCdf(d1) 
            - 
            getStrikePrice() * exp(-getRiskFreeRate() * getTimeToMaturity()) * normCdf(d2)
        );
        delta = normCdf(d1);
    } else {
        // Put option price
        price = (
            getStrikePrice() * exp(-getRiskFreeRate() * getTimeToMaturity()) * normCdf(-d2) 
            - 
            getUnderlyingPrice() * normCdf(-d1)
        );
        delta = normCdf(d1) - 1;
    }

    return std::make_pair(price, delta);

}