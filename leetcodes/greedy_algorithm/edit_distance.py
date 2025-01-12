# https://leetcode.com/problems/edit-distance/description/


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
