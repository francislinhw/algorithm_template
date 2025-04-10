# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        
        for i in reversed(range(len(text2))):
            for j in reversed(range(len(text1))):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                    # dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]