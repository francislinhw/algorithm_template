from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        res = 0
        seem = {}
    
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0

            if (i, j) in seem:
                return seem[(i, j)]
            up = 1 + dfs(i - 1, j, matrix[i][j])
            down = 1 + dfs(i + 1, j, matrix[i][j])
            left = 1 + dfs(i, j - 1, matrix[i][j])
            right = 1 + dfs(i, j + 1, matrix[i][j])
            total = max(up, down, left, right)
            seem[(i, j)] = total
            
            return seem[(i, j)]

        for i in range(m):
            for j in range(n):
                temp = dfs(i, j, -1)
                res = max(res, temp)
        
        return res
