# https://leetcode.com/problems/decode-ways/description/


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # 空字串有 1 種解碼方式
        dp[n - 1] = 1 if s[-1] != "0" else 0

        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if 10 <= int(s[i : i + 2]) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]


class Solution(object):
    def numDecodings(self, s):
        # 10.15
        if not s or s[0] == "0":
            return 0

        prev = curr = 1  # prev: dp[i-2], curr: dp[i-1]

        for i in range(1, len(s)):
            temp = 0
            if s[i] != "0":
                temp = curr
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                temp += prev
            prev, curr = curr, temp

        return curr


# class Solution(object):
#     def numDecodings(self, s):
#         if not s or s[0] == '0':
#             return 0

#         n = len(s)
#         dp = [0] * (n + 1)
#         dp[0] = 1  # 空字串有一種解法
#         dp[1] = 1  # 第一個字元不是 '0' 時，有一種解法

#         for i in range(2, n + 1):
#             one_digit = int(s[i-1])      # 單個字元
#             two_digits = int(s[i-2:i])   # 兩個字元

#             if 1 <= one_digit <= 9:
#                 dp[i] += dp[i - 1]
#             if 10 <= two_digits <= 26:
#                 dp[i] += dp[i - 2]

#         return dp[n]


class Solution:
    def numDecodings(self, s):

        if not s or s[0] == "0":  # 空字串或開頭是 0 無法解碼
            return 0

        oneBack = 1 if s[-1] != "0" else 0  # 最後一個字元，如果不是 '0'，就有 1 種解法
        twoBack = 1  # 空字串預設為 1 種解法

        # 從倒數第二個字開始往前走
        for i in reversed(range(len(s) - 1)):
            curr = 0
            if s[i] != "0":  # 單個字元不是 '0' 才能當一個字母
                curr = oneBack

                doubleDig = int(s[i : i + 2])  # 取兩個字元看看是不是合法（10~26）
                if 10 <= doubleDig <= 26:
                    curr += twoBack

            # 滾動更新狀態
            twoBack = oneBack
            oneBack = curr

        return oneBack


class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == "0":
            return
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # 空字串有一種解法
        dp[1] = 1  # 第一個字元不是 '0' 時，有一種解法
        for i in range(2, n + 1):
            one_digit = int(s[i - 1])  # 單個字元
            two_digits = int(s[i - 2 : i])  # 兩個字元
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]
        return dp[n]


class Solution:
    def numDecodings(self, s):

        if not s or s[0] == "0":  # 空字串或開頭是 0 無法解碼
            return 0

        oneBack = 1 if s[-1] != "0" else 0  # 最後一個字元，如果不是 '0'，就有 1 種解法
        twoBack = 1  # 空字串預設為 1 種解法

        # 從倒數第二個字開始往前走
        for i in reversed(range(len(s) - 1)):
            curr = 0
            if s[i] != "0":  # 單個字元不是 '0' 才能當一個字母
                curr = oneBack

                doubleDig = int(s[i : i + 2])  # 取兩個字元看看是不是合法（10~26）
                if 10 <= doubleDig <= 26:
                    curr += twoBack

            # 滾動更新狀態
            twoBack = oneBack
            oneBack = curr

        return oneBack


class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == "0":
            return 0

        oneBack = 1 if int(s[-1]) != 0 else 0
        twoBack = 1

        for i in reversed(range(len(s) - 1)):
            curr = 0
            if s[i] == "0":
                twoBack = oneBack
                oneBack = curr
                continue
            curr = oneBack

            doubleDig = int(s[i : i + 2])
            if 10 <= doubleDig <= 26:
                curr += twoBack
            twoBack = oneBack
            oneBack = curr
        return oneBack
