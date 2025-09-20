
#include "bond.hpp"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <cassert>

using namespace std;


int main() {
    
    // Test 1: Semi-annual bond (7% coupon, expiration 2035/11/19)
    Bond semiAnnualBond("11/19/2035", 0.5, 0.08);

    // Time to maturity	4.2
    // Frequency	0.5
    // Coupon rate	0.08
    // Interest rate	0.07

    assert(abs(semiAnnualBond.Price(0.07, 4.2) - 103.1449377) < 1e-6);
    cout << "Test 1 passed" << endl;

    // Test 2: Test Bond Constructor
    Bond bond("11/19/2035", 0.5, 0.08);
    assert(bond.ToString() == "Bond(11/19/2035, 0.5, 0.08)");
    cout << "Test 2 passed" << endl;


    cout << "All tests passed" << endl;
    return 0;
}
