#ifndef BOND_HPP
#define BOND_HPP
#include <vector>
#include <string>
using namespace std;

// struct to store zero rate curve data
struct RateData {
    double ttm;   // time to maturity
    double rate;  // zero rate
};

class Bond {
private:
    string expirationDate;
    double frequency;   // the number of times the bond is paid per year, for example 0.5 = half-yearly
    double couponRate;  // coupon rate on the bond

public:
    Bond();
    ~Bond();
    Bond(const Bond& other);
    Bond(string expDate, double freq, double coup);

    string ToString() const;

    // Pricing function
    double Price(double interest_rate, double years_to_maturity) const;

    static double Price(
        double faceValue,                         // face value
        double couponRate,                        // coupon rate
        int frequency,                            // frequency
        std::chrono::system_clock::time_point maturityDate,   // maturity date
        std::chrono::system_clock::time_point valuationDate,  // valuation date
        double flatRate                           // flat interest rate
    );

    // Forward price calculation (member function)
    double ForwardPrice(const vector<RateData>& rates,
            double forwardTime,
            double maturityTime) const;
};

#endif // BOND_HPP
