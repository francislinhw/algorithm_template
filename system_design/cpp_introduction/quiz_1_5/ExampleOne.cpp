#include <iostream>
#include <string>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <vector>
#include <utility>
#include <tuple>
#include <functional> // for std::hash

using namespace std;


int main() { // session 1 basic

    // useful data types
    int a = 1;
    double b = 2.0;
    char c = 'c';
    bool d = true;
    string e = "Hello, World!";
    vector<int> f = {1, 2, 3, 4, 5};
    map<int, string> g = {{1, "Hello"}, {2, "World"}};
    set<int> h = {1, 2, 3, 4, 5};
    list<int> k = {1, 2, 3, 4, 5};
    pair<int, string> l = {1, "Hello"};
    tuple<int, string, double> m = {1, "Hello", 2.0};
    string s = "Hello, World!";
    cout << s << endl;
    cout << s.size() << endl;
    cout << s.length() << endl;
    cout << s.capacity() << endl;
    cout << s.max_size() << endl;
    cout << s.empty() << endl;
    cout << s.front() << endl;

    // argc and argv 
    // argc is the number of arguments
    // argv is the arguments

    // control flow
    // if statement
    if (a > b) {
        cout << "a is greater than b" << endl;
    } else {
        cout << "a is less than b" << endl;
    }

    // for loop
    for (int i = 0; i < 10; i++) {
        cout << i << endl;
    }

    // while loop
    while (a < 10) {
        cout << a << endl;
        a++;
    }

    // do while loop
    // << , >>
    // << is left shift
    // >> is right shift
    cout << a << b << endl;
    cout << a << b << endl;

    // ifstreaminfile(“filename”); // input file
    // ofstream outfile(“filename”); // output file
    // fstream inoutfile(“filename”); // in/output

    // String concatenation
    string s1 = "Hello";
    string s2 = "World";
    string s3 = s1 + s2;
    cout << s3 << endl;

    // string is the vector of characters
    vector<char> s4 = {'H', 'e', 'l', 'l', 'o'};
    string s4_str(s4.begin(), s4.end());  // Convert vector<char> to string
    cout << s4_str << endl;

    string s5 = "Hello";

    if (s5 == s4_str) {
        cout << "s5 is equal to s4" << endl;
    } else {
        cout << "s5 is not equal to s4" << endl;
    }

    // String manipulations functions
    cout << s5.size() << endl;
    cout << s5.length() << endl;
    cout << s5.capacity() << endl;
    cout << s5.max_size() << endl;
    cout << s5.empty() << endl;
    cout << s5.front() << endl;
    cout << s5.back() << endl;
    cout << s5.find('o') << endl;
    cout << s5.find('o', 5) << endl;

    // hash function
    cout << hash<string>{}(s5) << endl;

    // substr function
    cout << s5.substr(0, 5) << endl;
    cout << s5.substr(5) << endl;

    // find function
    cout << s5.find('o') << endl;
    cout << s5.find('o', 5) << endl;

    // replace function
    cout << s5.replace(0, 5, "World") << endl;

    // insert function
    cout << s5.insert(0, "World") << endl;

    // erase function
    cout << s5.erase(0, 5) << endl;

    // append function
    cout << s5.append("World") << endl;

    // r find function: it is to find the last occurrence of the character
    cout << s5.rfind('o') << endl;
    cout << s5.rfind('o', 5) << endl;

    string x="FROM:deng@gatech.edu";
    int colonPos=x.find(':');
    string prefix=x.substr(0,colonPos); //=FROM
    string suffix = x.substr(colonPos+1);
    cout<<"-This message is from "<<suffix<<endl;

    // reverse a string
    for (int i = s5.size() - 1; i >= 0; i--) {
        cout << s5[i];
    }
    cout << endl;

    // reverse a string using reverse function
    reverse(s5.begin(), s5.end());
    cout << s5 << endl;
    return 0;
}
// session 2 parentheses
#include <iostream>
#include <string>
using namespace std;

class ChkString {
public:
    bool checkValidString(string s) {
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
// session 3: valid parentheses

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


// session 4 reverse words
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    // find all spaces
    vector<int> findSpace(const string& s) {
        vector<int> space_vec;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') {
                space_vec.push_back(i);
            }
        }
        return space_vec;
    }

    // reverse sentence according to the space position
    string reverseSentence(const string& s, const vector<int>& space_vec) {
        string result = "";
        int n = space_vec.size();

        // the last word
        result += s.substr(space_vec[n - 1] + 1);

        // the middle words
        for (int i = n - 2; i >= 0; i--) {
            result += " ";
            result += s.substr(space_vec[i] + 1, space_vec[i + 1] - space_vec[i] - 1);
        }

        // the first word
        result += " ";
        result += s.substr(0, space_vec[0]);

        return result;
    }

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

        // Step 3. find the space position
        vector<int> space_vec = findSpace(temp);

        // if there is no space, return the original string
        if (space_vec.empty()) return temp;

        // Step 4. reverse the sentence
        return reverseSentence(temp, space_vec);
    }
};

int main() {
    Solution sol;
    cout << sol.reverseWords("  I   love   C++  ") << endl;
    // Output: "C++ love I"
}



