#include "Option.h"

// Initialize default parameters
void Option::init() {
    K = 100.0;
    S = 100.0;
    r = 0.05;
    T = 1.0;
    sigma = 0.2;
}

// Default constructor
Option::Option() {
    init();
}

// Parameterized constructor
Option::Option(double strike, double underlyingPrice, double riskFreeRate, double timeToMaturity, double volatility) 
    : K(strike), S(underlyingPrice), r(riskFreeRate), T(timeToMaturity), sigma(volatility) {}

// Destructor
Option::~Option() {}

// Get methods for each parameter
double Option::getK() const { return K; }
double Option::getS() const { return S; }
double Option::getR() const { return r; }
double Option::getT() const { return T; }
double Option::getSigma() const { return sigma; }