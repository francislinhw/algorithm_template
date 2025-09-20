#include <string>
#include <ostream>
#include <iostream>
using namespace std;


class Solution {
    public:
        bool isAnagram(string s, string t) {
            if (s.size() != t.size()) return false;
    
            int count[26] = {0};
    
            for (char c : s) count[c - 'a']++;
            for (char c : t) count[c - 'a']--;
    
            for (int i = 0; i < 26; i++) {
                if (count[i] != 0) return false;
            }
            return true;
        }
    };

int main() {
    Solution sol;
    string s = "anagram";
    string t = "nagaram";
    cout << sol.isAnagram(s, t) << endl;
    return 0;
}