# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.cnt = 0
        self.result = ""

        def checkPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.cnt += 1
                if len(self.result) < (r - l + 1):
                    self.result = s[l:r+1]

                l -= 1
                r += 1
            return 

        for i in range(len(s)):
            l = i
            r = i
            checkPalindrome(l, r)
            l = i
            r = i + 1
            checkPalindrome(l, r)
        return self.result
        