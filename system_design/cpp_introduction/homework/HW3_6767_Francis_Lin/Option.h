#ifndef OPTION_H
#define OPTION_H

class Option {
private:
    double K;      // Strike price
    double S;      // Current price of underlying asset
    double r;      // Risk-free rate
    double T;      // Time to maturity
    double sigma;  // Volatility

    void init();  // Private method to initialize default parameters

public:
    // Default constructor
    Option();

    // Parameterized constructor
    Option(double strike, double underlyingPrice, double riskFreeRate, double timeToMaturity, double volatility);

    // Destructor
    ~Option();

    // Get methods for each parameter
    double getK() const;
    double getS() const;
    double getR() const;
    double getT() const;
    double getSigma() const;
};

#endif // OPTION_H