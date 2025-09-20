# https://leetcode.com/problems/triangle/

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 從底部往上推，每次覆蓋上一層
        dp = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
        return dp[0]
