#include "util.hpp"
#include <numeric>   // for accumulate

// Compute average
double average(const std::vector<double>& v) {
    if (v.empty()) return 0.0;
    double sum = std::accumulate(v.begin(), v.end(), 0.0);
    return sum / v.size();
}

// Find rate by date
double find_rate(const std::vector<double>& rate_vec,
                 const std::vector<std::string>& date_vec,
                 const std::string& date) {
    for (size_t i = 0; i < date_vec.size(); i++) {
        if (date_vec[i] == date) {
            return rate_vec[i];
        }
    }
    return -1.0; // not found
}
