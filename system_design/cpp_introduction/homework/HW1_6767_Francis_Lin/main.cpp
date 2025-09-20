#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include "util.hpp"

// using namespace std; Not recommended since self-defined functions are possible to have the same name as the standard library functions

int main() {
    std::vector<double> rate;
    std::vector<std::string> date;
    std::ifstream infile("hw1_H.15_Baa_Data.csv");

    if (!infile.is_open()) {
        std::cerr << "File not found!" << std::endl; // cerr is for error output
        return 1;
    }

    std::string line;
    // Skip first 6 lines
    for (int i = 0; i < 6 && getline(infile, line); i++);

    // Start reading data
    while (getline(infile, line)) {
        std::stringstream ss(line);
        std::string d, r;
        if (getline(ss, d, ',') && getline(ss, r, ',')) {
            date.push_back(d);
            try {
                rate.push_back(stod(r));
            } catch (...) {
                std::cerr << "Bad rate format at line: " << line << std::endl;
            }
        }
    }
    infile.close();

    // Average
    double avg = average(rate);

    // Query loop
    std::string query;
    std::cout << "Enter date (yyyy-mm), Ctrl+D to quit:" << std::endl;
    while (std::cin >> query) {
        double r = find_rate(rate, date, query);
        if (r < 0) {
            std::cout << "Date not found." << std::endl;
        } else {
            std::cout << "Rate = " << r << ", diff from avg = " << r - avg << std::endl;
        }
        std::cout << "Enter date (yyyy-mm), Ctrl+D to quit:" << std::endl;
    }

    return 0;
}
