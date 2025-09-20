#include <iostream>
#include <string>
using namespace std;

class ChkString {
public:
    bool checkValidString(string s) {
    /* Function implementation code starts here */
        int left = 0, right = 0, all = 0, flag = 2;
        for (char c : s) {
            if (c == '(') {
                left++;
            } else if (c == ')') {
                right++;
            } else {
                all++;
            }
            if (right > left + all) {
                return false;
            }
        }
        if (s[s.size() - 1] == '(') {
            return false;
        }

        int absolute_value;
        if (left - right < 0){
            absolute_value = right - left;
        }
        else{
            absolute_value = left - right;
        }

        if (absolute_value == 0){
            return true;
        }
        else if(all - absolute_value >= 0 && (all - absolute_value) % 2 == 0){
            return true;
        }
        else{
            return false;
        }
    
    /* code ends here */       
    }
};


int main() {
    ChkString sol;
    string s = "(**)";
    cout << sol.checkValidString(s) << endl;  // Output: TRUE or FALSE
    return 0;
}


