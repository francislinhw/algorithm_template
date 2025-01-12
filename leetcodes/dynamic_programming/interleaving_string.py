# https://leetcode.com/problems/interleaving-string/submissions/1490777153/

from typing import List

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        dp = []
        for i in range(len(s1)+1):
            tmp = []
            for j in range(len(s2)+1):
                tmp.append(False)
            dp.append(tmp)
        dp[-1][-1] = True
        
        for i in reversed(range(len(s1)+1)):
            for j in reversed(range(len(s2)+1)):
                if i+1 <= len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j+1 <= len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Len = len(s1)
        s2Len = len(s2)
        s3Len = len(s3)

        if s1Len + s2Len != s3Len:
            return False
        
        grid = [[False for i in range(s1Len + 1)] for j in range(s2Len + 1)]
        grid[s1Len][s2Len] = True

        s3Position = s3Len - 2

        for r in reversed(range(s1Len)):
            for c in reversed(range(s2Len)):
                subS3 = s3[s3Position + 2]
                if (subS3 == s1[r] + s2[c] or subS3 == s2[c] + s1[r]):
                    grid[r][c] = True
                    s3Position -= 2
        
        

        return grid[0][0] if s3Position == 0 else False
