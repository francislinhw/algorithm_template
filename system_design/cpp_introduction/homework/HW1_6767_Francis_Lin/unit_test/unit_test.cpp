#include <cassert>
#include <vector>
#include <string>
#include "../util.hpp"
#include <iostream>

int main() {
    // Test average
    std::vector<double> v1 = {1.0, 2.0, 3.0};
    assert(average(v1) == 2.0);

    std::vector<double> v2;
    assert(average(v2) == 0.0);

    // Test find_rate
    std::vector<double> rates = {1.5, 2.0, 2.5};
    std::vector<std::string> dates = {"2019-01", "2019-02", "2019-03"};

    assert(find_rate(rates, dates, "2019-02") == 2.0);
    assert(find_rate(rates, dates, "2019-01") == 1.5);
    assert(find_rate(rates, dates, "2019-03") == 2.5);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
