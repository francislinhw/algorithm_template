#include <string>
#include <iostream>
using namespace std;

class Solution {
    public:
        bool isPalindrome(int x) {
            if (x < 0) return false; 
            long long rev = 0, temp = x;
            while (temp > 0) {
                rev = rev * 10 + temp % 10;
                temp /= 10;
            }
            return rev == x;
        }
    };
    
class Solution2 {
    public:
        bool isPalindrome(string s) {
            int l = 0, r = s.size() - 1;
            while (l < r) {
                while (l < r && !isalnum(s[l])) l++;
                while (l < r && !isalnum(s[r])) r--;
                if (tolower(s[l]) != tolower(s[r])) return false;
                l++;
                r--;
            }
            return true;
        }
    };
    
int main() {
    Solution sol;
    string s = "A man, a plan, a canal: Panama";
    cout << sol.isPalindrome(s) << endl;
    return 0;
}