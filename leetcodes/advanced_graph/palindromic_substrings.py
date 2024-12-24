# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        # def checkPalidromic(strig: str):
        #     l = 0
        #     r = len(string)

        #     isSame = True

        #     while l <= r:
        #         first = string[l]
        #         second = string[r]

        #         if first != second:
        #             isSame = False

        #         l += 1
        #         r -= 1

        #     return isSame

        self.cnt = 0
        def checkPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.cnt += 1
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
        return self.cnt
        