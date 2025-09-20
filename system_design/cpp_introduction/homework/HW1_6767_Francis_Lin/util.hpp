#ifndef UTIL_HPP // ifndef is for header guard
#define UTIL_HPP

#include <vector>
#include <string>

// Compute average of vector<double>
double average(const std::vector<double>& v);

// Find rate by date
double find_rate(const std::vector<double>& rate_vec,
                 const std::vector<std::string>& date_vec,
                 const std::string& date);

#endif // UTIL_HPP
