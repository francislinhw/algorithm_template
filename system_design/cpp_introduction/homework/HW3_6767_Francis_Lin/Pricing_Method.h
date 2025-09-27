#ifndef PRICING_METHOD_H
#define PRICING_METHOD_H

class Pricing_Method {
public:
    virtual double BSM_Pricer() const = 0;  // Pure virtual function to calculate price using Black-Scholes
    virtual double BSM_Delta() const = 0;   // Pure virtual function to calculate delta using Black-Scholes

    virtual double Binomial_Pricer() const = 0;  // Pure virtual function to calculate price using Binomial model
    virtual double Binomial_Delta() const = 0;   // Pure virtual function to calculate delta using Binomial model

    virtual ~Pricing_Method() = default;  // Virtual destructor
};

#endif // PRICING_METHOD_H