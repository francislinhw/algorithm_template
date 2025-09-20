#include <iostream>
#include <string>
using namespace std;

void reverseManual(string& s, int left, int right) {
    while (left < right) {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }
}

class Solution {
public:
    string reverseWords(string s) {
        // Step 1. remove leading and trailing spaces
        int left = 0, right = s.size() - 1;
        while (left <= right && s[left] == ' ') left++;
        while (left <= right && s[right] == ' ') right--;

        // Step 2. compress multiple spaces into one space in between words
        string temp = "";
        for (int i = left; i <= right; i++) {
            if (s[i] != ' ') {
                temp += s[i];
            } else if (temp.back() != ' ') {
                temp += ' ';
            }
        }

        // Step 3. reverse the whole string
        reverseManual(temp, 0, temp.size() - 1);

        // Step 4. 再逐個單字反轉
        int start = 0;
        for (int i = 0; i <= temp.size(); i++) {
            if (i == temp.size() || temp[i] == ' ') {
                reverseManual(temp, start, i - 1);
                start = i + 1;
            }
        }

        return temp;
    }
};

int main() {
    Solution sol;
    cout << sol.reverseWords("  I   love   C++  ") << endl;
    // Output: "C++ love I"
}
