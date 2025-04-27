# https://leetcode.com/problems/edit-distance/description/


class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        dp = [
            [0] * (n + 1) for _ in range(m + 1)
        ]  # 建立 DP 表格 dp[i][j] 代表 word1 前 i 個字 和 word2 前 j 個字的最小編輯距離

        for i in range(m + 1):
            dp[i][0] = i  # 將 word1[0:i] 全部刪掉
        for j in range(n + 1):
            dp[0][j] = j  # 將 word2[0:j] 全部插入

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 字元相同，不用操作
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # 刪除
                        dp[i][j - 1] + 1,  # 插入
                        dp[i - 1][j - 1] + 1,  # 替換
                    )

        return dp[m][n]


# 13 March 2025 Practice
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 10.49
        # Step 1: pre processing for DP
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        dp = []

        for i in range(len(word1) + 1):
            dp.append([])

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if j == len(word2):
                    dp[i].append(len(word1) - i)
                else:
                    dp[i].append(float("inf"))

        for j in range(len(word2) + 1):
            dp[-1][j] = len(word2) - j

        for i in reversed(range(len(dp) - 1)):
            for j in reversed(range(len(dp[i]) - 1)):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert = 1 + dp[i][j + 1]
                    delete = 1 + dp[i + 1][j]
                    replace = 1 + dp[i + 1][j + 1]
                    dp[i][j] = min(delete, insert, replace)

        return dp[0][0]  # 11.04


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = []
        for i in range(len(word1) + 1):
            tmp = []
            for j in range(len(word2) + 1):
                tmp.append(float("inf"))
            dp.append(tmp)

        for i in range(len(word1) + 1):
            dp[i][-1] = len(word1) - i

        for j in range(len(word2) + 1):
            dp[-1][j] = len(word2) - j

        for i in reversed(range(len(word1))):
            for j in reversed(range(len(word2))):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert = 1 + dp[i][j + 1]
                    delete = 1 + dp[i + 1][j]
                    replace = 1 + dp[i + 1][j + 1]
                    dp[i][j] = min(insert, delete, replace)
        return dp[0][0]


# Example

# word1 = "horse"
# word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

sol = Solution()
print(sol.minDistance("abc", "adc"))

# we shold update the dp table

# dp = [
#     [1, 2, 2, 3],
#     [2, 1, 1, 2],
#     [2, 1, 0, 1],
#     [3, 2, 1, 0],
# ]

# Output: 3
