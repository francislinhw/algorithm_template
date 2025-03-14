# https://leetcode.com/problems/valid-parenthesis-string/description/


# 12 March 2025 Practice
class Solution:
    def checkValidString(self, s: str) -> bool:
        # 11.08
        if len(s) == 1:
            if s[0] != "*":
                return False
            return True

        leftParenMax = 0
        leftParenMin = 0

        for p in s:
            if p == "(":
                leftParenMax += 1
                leftParenMin += 1
            elif p == ")":
                leftParenMax -= 1
                leftParenMin -= 1
            elif p == "*":
                leftParenMax += 1  # treat as (
                leftParenMin -= 1  # treat as )

            if leftParenMax < 0:
                return False
            if leftParenMin < 0:
                leftParenMin = 0

        return True if leftParenMin == 0 else False  # 11.15


class Solution:
    def checkValidString(self, s: str) -> bool:

        leftMin = 0  # 左括號最小數量
        leftMax = 0  # 左括號最大數量

        for char in s:

            if char == "(":
                leftMin += 1
                leftMax += 1
            elif char == ")":  # 遇到右括號，左括號數量減一
                leftMin -= 1
                leftMax -= 1
            elif char == "*":  # * 可以當作 ( 或 ) 或 空字串
                leftMin -= 1  # * 當作 ), 左括號數量減一
                leftMax += 1  # * 當作 ( , 左括號數量加一
                # * 當作空字串 do nothing

            if leftMax < 0:  # 左括號數量為負，表示右括號數量過多，無法平衡
                return False
            # 如何思考這個條件？
            # 因為 * 可以當作空字串，所以 leftMin 最小為 0
            # 如果 leftMin 為負，表示 * 當作 ) 的數量過多，無法平衡
            # 所以 leftMin 最小為 0
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
