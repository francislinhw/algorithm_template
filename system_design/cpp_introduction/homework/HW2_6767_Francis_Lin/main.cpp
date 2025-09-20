
#include "bond.hpp"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

/************ Date struct to deal with the date calculation ************/


// Date struct to deal with the date calculation
struct Date {
    int year, month, day;
};


bool isLeap(int y) {
    return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
}

int daysInMonth(int y, int m) {
    static int days[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    if (m == 2 && isLeap(y)) return 29;
    return days[m-1];
}

int toDays(const Date& d) {
    int days = d.day;
    for (int y = 1900; y < d.year; y++) {
        days += isLeap(y) ? 366 : 365;
    }
    for (int m = 1; m < d.month; m++) {
        days += daysInMonth(d.year, m);
    }
    return days;
}

double yearFraction(const Date& d1, const Date& d2) {
    int diff = toDays(d2) - toDays(d1);
    return diff / 365.0;  // Actual/365
}
/************************ End of Date struct to deal with the date calculation ************/

/************ find the closest rate (corresponding to a TTM) ************/

double findRate(const vector<RateData>& data, double targetTTM) {
    double closestRate = 0.0;
    double minDiff = 1e9;

    for (auto& d : data) {
        double diff = fabs(d.ttm - targetTTM);
        if (diff < minDiff) {
            minDiff = diff;
            closestRate = d.rate;
        }
    }
    return closestRate;
}

// calculate the present value
double SecurityPV(double avgPrice, double rate, double ttm) {
    return avgPrice * exp(-rate * ttm);
}

/************************ End of find the closest rate (corresponding to a TTM) ************/

/************ read the CSV file ************/

vector<RateData> readCSV(const string& filename) {
    vector<RateData> data;
    ifstream file(filename);
    string line;

    while (getline(file, line)) {
        stringstream ss(line);
        string ttmStr, rateStr;
        if (getline(ss, ttmStr, ',') && getline(ss, rateStr, ',')) {
            try {
                double ttm = std::stod(ttmStr); // stod is to convert the string to double, from standard library
                double rate = std::stod(rateStr);
                data.push_back({ttm, rate});
            } catch (...) {
                // skip the title or the wrong format line
                continue;
            }
        }
    }
    return data;
}

/************************ End of read the CSV file ************/

int main() {

    cout << "Problem 1" << endl;
    // problem 1: Semi-annual bond (7% coupon, expiration 2035/11/19)
    Bond semiAnnualBond("11/19/2035", 0.5, 0.07);
    cout << "Bond Information: " << endl;
    cout << semiAnnualBond.ToString() << endl;

    cout << endl;
    cout << endl;
    cout << "Problem 2" << endl;

    // problem 2: assume the rate r = 7%, the duration = 10 years
    Bond semiAnnualBondTest("11/19/2035", 0.5, 0.08);
    // Time to maturity	4.2
    double duration = 4.2;
    double price = semiAnnualBondTest.Price(0.07, duration);
    cout << "Bond Price (r=7%, 10y): " << price << endl;



    //  valuation date (2025/01/01) and maturity date (2028/01/01)
    std::tm valuation_tm = {};
    valuation_tm.tm_year = 2025 - 1900; // the year from 1900
    valuation_tm.tm_mon = 0;            // 0 = January
    valuation_tm.tm_mday = 1;
    auto valuationDate = std::chrono::system_clock::from_time_t(std::mktime(&valuation_tm));

    std::tm maturity_tm = {};
    maturity_tm.tm_year = 2028 - 1900;
    maturity_tm.tm_mon = 0;
    maturity_tm.tm_mday = 1;
    auto maturityDate = std::chrono::system_clock::from_time_t(std::mktime(&maturity_tm));

    // Bond parameters
    double faceValue = 100.0;
    double couponRate = 0.05; // 5%
    int frequency = 1;        // once a year

    // ------------------------------
    // Example 1: Updated Pricing function with specific parameters
    // ------------------------------
    double flatRate = 0.04; // 4%
    double priceFlat = Bond::Price(faceValue, couponRate, frequency, maturityDate, valuationDate, flatRate); 
    std::cout << "Bond price with flat rate (4%): " << priceFlat << std::endl;

    // problem 3: 
    cout << endl;
    cout << endl;
    cout << "Problem 3" << endl;
    Bond semiAnnualBond2("1/1/2010", 0.5, 0.05);
    // step 1: read the file
    string filename = "Bond_Ex3.csv";  
    vector<RateData> rates = readCSV(filename);

    if (rates.empty()) {
        cerr << "Read CSV failed or the file is empty!" << endl;
        return 1;
    }

    // calculate maturityTime
    Date start{2015, 8, 3};     // investment date
    Date maturity{2020, 12, 31}; // payoff date
    double maturityTime = yearFraction(start, maturity);

    // calculate forward dates
    vector<Date> forwardDates = {
        {2016, 12, 31},
        {2017, 12, 31},
        {2018, 12, 31},
        {2019, 12, 31},
        {2020, 12, 31}
    };

    vector<double> forwardTimes;
    for (auto& fd : forwardDates) {
        forwardTimes.push_back(yearFraction(start, fd));
    }

    cout << "Forward Times: ";
    for (auto f : forwardTimes) cout << f << " ";
    cout << endl;


    vector<double> bondPrices;
    for (double f : forwardTimes) {
        double price = semiAnnualBond2.ForwardPrice(rates, f, maturityTime);
        bondPrices.push_back(price);
    }

    cout << "Forward Prices: ";
    for (auto p : bondPrices) cout << p << " ";
    cout << endl;
    double sum = 0.0;
    for (double p : bondPrices) sum += p;
    double avgPrice = sum / bondPrices.size();

    // step 3: find the TTM rate of 2015/8/3 to 2020/12/31
    double timeToMaturity = maturityTime;
    double rate = findRate(rates, timeToMaturity);

    // step 4: discount back
    double pv = SecurityPV(avgPrice, rate, timeToMaturity);

    cout << "Average Price (2016-2020): " << avgPrice << endl;
    cout << "Discount Rate (approx): " << rate << endl;
    cout << "Present Value: " << pv << endl;
    
    double cost = 98.0;
    cout << "Investment Cost: " << cost << endl;

    if (pv > cost)
        cout << "Good Investment!" << endl;
    else
        cout << "Not a Good Investment!" << endl;

    return 0;
}
