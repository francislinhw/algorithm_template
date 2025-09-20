#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    // 找到所有空格的位置
    vector<int> findSpace(const string& s) {
        vector<int> space_vec;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') {
                space_vec.push_back(i);
            }
        }
        return space_vec;
    }

    // 根據空格位置反轉句子
    string reverseSentence(const string& s, const vector<int>& space_vec) {
        string result = "";
        int n = space_vec.size();

        // 最後一個單字
        result += s.substr(space_vec[n - 1] + 1);

        // 中間單字
        for (int i = n - 2; i >= 0; i--) {
            result += " ";
            result += s.substr(space_vec[i] + 1, space_vec[i + 1] - space_vec[i] - 1);
        }

        // 第一個單字
        result += " ";
        result += s.substr(0, space_vec[0]);

        return result;
    }

    string reverseWords(string s) {
        // Step 1. 移除前後空白
        int left = 0, right = s.size() - 1;
        while (left <= right && s[left] == ' ') left++;
        while (left <= right && s[right] == ' ') right--;

        // Step 2. 壓縮多餘空白
        string temp = "";
        for (int i = left; i <= right; i++) {
            if (s[i] != ' ') {
                temp += s[i];
            } else if (temp.back() != ' ') {
                temp += ' ';
            }
        }

        // Step 3. 找出空格位置
        vector<int> space_vec = findSpace(temp);

        // 如果沒有空格，直接回傳
        if (space_vec.empty()) return temp;

        // Step 4. 反轉句子
        return reverseSentence(temp, space_vec);
    }
};

int main() {
    Solution sol;
    cout << sol.reverseWords("  I   love   C++  ") << endl;
    // Output: "C++ love I"
}
