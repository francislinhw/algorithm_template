# https://leetcode.com/problems/distinct-subsequences/


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
