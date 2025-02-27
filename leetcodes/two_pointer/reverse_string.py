# https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 8.54 two pointers

        if not s:
            return s

        length = len(s)

        l = 0
        r = length - 1

        while r > l:
            print(l)
            print(r)
            rightValue = s[r]
            leftValue = s[l]

            s[r] = leftValue
            s[l] = rightValue

            l += 1
            r -= 1

        return None  # 6 min

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        returnS = s

        lPtr = 0
        rPtr = len(s) - 1

        while lPtr < rPtr:
            returnS[lPtr] = s[rPtr]
            returnS[rPtr] = s[lPtr]

        return returnS
