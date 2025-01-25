# https://leetcode.com/problems/valid-parenthesis-string/description/


class Solution:
    def checkValidString(self, s: str) -> bool:

        leftMin = 0
        leftMax = 0

        for char in s:

            if char == "(":
                leftMin += 1
                leftMax += 1
            elif char == ")":
                leftMin -= 1
                leftMax -= 1
            else:  # *
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False
            if leftMin < 0:  # in case ))((
                leftMin = 0
        return leftMin == 0
