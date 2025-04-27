# https://leetcode.com/problems/distinct-subsequences/
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 空字串 t，只能有 1 種方式（什麼都不選）
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # 用 s[i-1] 拼 t[j-1] + 不用它
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # 不用它，跳過這個字
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]


class Solution(object):
    def numDistinct(self, s, t):
        # 5.19
        m, n = len(s), len(t)
        if n == 0:  # t 為空 → 只有 1 種
            return 1
        if m < n:  # s 比 t 短 → 不可能
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # 空字串基底

        for i in range(1, m + 1):
            # 必須從後往前，確保上一輪 dp[j-1] 尚未被覆蓋
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                # else: dp[j] 不變（等於上一輪的 dp[j]）

        return dp[n]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # Create a 2D DP array of size (m+1) x (n+1) initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: If t is empty, there is exactly one way to match it (by deleting all characters in s)
        for i in range(m + 1):
            dp[i][n] = 1
        print(dp)

        # Fill the DP table in reverse order
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    # If characters match, we can either include s[i] or skip it
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]  # + dp[i+1][j]
                else:
                    # If they don't match, we skip s[i] and move forward
                    dp[i][j] = dp[i + 1][j]

        # The final result will be in dp[0][0], representing how many ways s[0:] matches t[0:]
        return dp[0][0]
