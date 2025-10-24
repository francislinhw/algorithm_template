#include <iostream>
#include <vector>

using namespace std;

class Bank {
public:
vector<long long>& balance_ref;
// Initialize the Bank with an array of account balances by reference
Bank(vector<long long>& balance) : balance_ref(balance) {

}
// Transfers money from account1 to account2
bool transfer(int account1, int account2, long long money) {
/* Your code for the transfer function starts here */
if (account1 < 1 || account1 > balance_ref.size() || account2 < 1 || account2 > balance_ref.size()) {
return false;
}

int account1Index = account1 - 1;
int account2Index = account2 - 1;

if (balance_ref[account1Index] >= money && money >= 0) { // Zero is also valid
balance_ref[account1Index] -= money;
balance_ref[account2Index] += money;
return true;
}

return false;
/* Your code for the transfer function ends here */
}
// Deposits money into the specified account
bool deposit(int account, long long money) {
/* Your code for the deposit function starts here */
if (account < 1 || account > balance_ref.size() || money < 0) {
return false;
}
int accountIndex = account - 1;
balance_ref[accountIndex] += money;
return true;
/* Your code for the deposit function ends here */
}
// Withdraws money from the specified account
bool withdraw(int account, long long money) {
/* Your code for the withdraw function starts here */
if (account < 1 || account > balance_ref.size() || money < 0) {
return false;
}
int accountIndex = account - 1;

if (balance_ref[accountIndex] < money && money > 0) {
return false;
}

if (balance_ref[accountIndex] >= money) {
balance_ref[accountIndex] -= money;
return true;
}
return false;

/* Your code for the withdraw function ends here */
}

};

int main() {
vector<long long> balance = {10, 100, 20, 50, 30};
Bank bank(balance);
cout << bank.withdraw(3, 10) << endl; // Output: 1 true
cout << bank.transfer(5, 1, 20) << endl; // Output: 1 true
cout << bank.deposit(5, 20) << endl; // Output: 1 true
cout << bank.transfer(3, 4, 15) << endl; // Output: 0 false
cout << bank.withdraw(10, 50) << endl; // Output: 0 false
return 0;
}