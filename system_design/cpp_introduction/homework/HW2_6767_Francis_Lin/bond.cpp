#include "bond.hpp"
#include <sstream>
#include <cmath>

// Constructors
Bond::Bond() : expirationDate(""), frequency(0.0), couponRate(0.0) {}
Bond::~Bond() {}
Bond::Bond(const Bond& other) {
    expirationDate = other.expirationDate;
    frequency = other.frequency;
    couponRate = other.couponRate;
}
Bond::Bond(string expDate, double freq, double coup)
    : expirationDate(expDate), frequency(freq), couponRate(coup) {}

string Bond::ToString() const {
    ostringstream oss;
    oss << "Bond(" << expirationDate << ", "
        << frequency << ", "
        << couponRate << ")";
    return oss.str();
}

// Bond Pricing Function
double Bond::Price(double interest_rate, double years_to_maturity) const {
    double bond_price = 0.0;
    double face_value = 100.0;
    double coupon_payment = face_value * couponRate / (1.0 / frequency);

    if (years_to_maturity > 0) {
        
    // Calculate the present value of all coupon payments（except the last payment）
    int total_payments = static_cast<int>(years_to_maturity / frequency);
    for (int i = 1; i <= total_payments; ++i) {
        double discount_factor = std::exp(- interest_rate * frequency * i);
        bond_price += coupon_payment * discount_factor;
        // std::cout << bond_price << std::endl;
    }

    // Add the present value of the payment at maturity
    double final_discount_factor = std::exp(- interest_rate * years_to_maturity);
    double final_coupon_payment = face_value * couponRate * (years_to_maturity - total_payments * frequency);
    bond_price += (face_value + final_coupon_payment) * final_discount_factor;

    return bond_price;
    } // if time to maturity is greater than 0, calculate the bond price
    else {
        return face_value + coupon_payment;
    } // if time to maturity is 0, return the face value plus the coupon payment as the bond price
}

double Bond::Price(
    double faceValue,
    double couponRate,
    int frequency,
    std::chrono::system_clock::time_point maturityDate,
    std::chrono::system_clock::time_point valuationDate,
    double flatRate
) {
    auto duration = maturityDate - valuationDate;
    double yearsToMaturity =
        std::chrono::duration_cast<std::chrono::hours>(duration).count() /
        (24.0 * 365.0);

    if (yearsToMaturity <= 0.0) return faceValue;

    double bondPrice = 0.0;
    double couponPayment = faceValue * couponRate / frequency;

    // the payment time of each period
    for (int i = 1; ; ++i) {
        double paymentTime = i / static_cast<double>(frequency);
        if (paymentTime > yearsToMaturity) break;  // if the payment time is greater than the years to maturity, stop

        double discountFactor = std::exp(-flatRate * paymentTime);
        bondPrice += couponPayment * discountFactor;
    }

    // the last payment: maybe stub
    double lastPaymentTime = yearsToMaturity;
    double finalDiscountFactor = std::exp(-flatRate * lastPaymentTime);

    // the last payment: face + maybe stub coupon
    double stubCoupon = faceValue * couponRate * 
                        (yearsToMaturity * frequency -
                         static_cast<int>(yearsToMaturity * frequency)) / frequency;

    bondPrice += (faceValue + stubCoupon + couponPayment) * finalDiscountFactor;

    return bondPrice;
}


double Bond::ForwardPrice(const vector<RateData>& rates,
    double forwardTime,
    double maturityTime) const {

    /************ Forward Price Calculation ************/

    double priceNumerator = 0.0;
    double coupon = 100 * couponRate * frequency;

    if (fabs(forwardTime - maturityTime) < 1e-6) {
        return 100 + coupon;
    }
    int n = static_cast<int>(maturityTime / frequency + 0.5); // round up, to avoid missing the last period

    for (int i = 1; i <= n; i++) {
        double t = i * frequency;
        if (t < forwardTime) continue; // only skip the strictly less than forwardTime

        // find the zero rate of t
        double closestRate = 0.0;
        double minDiff = 1e9;
        for (auto& d : rates) {
            double diff = fabs(d.ttm - t);
            if (diff < minDiff) {
                minDiff = diff;
                closestRate = d.rate;
            }
        }
        double discountFactor = exp(-closestRate * t);
        double cashFlow = (i == n) ? (100 + coupon) : coupon;
        priceNumerator += cashFlow * discountFactor;
    }

    // denominator = valuation → forward 的 discount factor
    double closestRateF = 0.0;
    double minDiffF = 1e9;

    for (auto& d : rates) {
        double diff = fabs(d.ttm - forwardTime);
        if (diff < minDiffF) {
            minDiffF = diff;
            closestRateF = d.rate;
        }
    }
    double discountForward = exp(-closestRateF * forwardTime);

    return priceNumerator / discountForward;
}
