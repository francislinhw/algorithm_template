# https://leetcode.com/problems/minimum-path-sum/


class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]

        # res = [float("inf")]

        # def dfs(x, y, total):
        #     if x >= len(grid[0]) or y >= len(grid):
        #         return

        #     total += grid[y][x]

        #     if x == len(grid[0]) - 1 and y == len(grid) - 1:
        #         res[0] = min(res[0], total)
        #         return

        #     dfs(x + 1, y, total)
        #     dfs(x, y + 1, total)

        # dfs(0, 0, 0)
        # return res[0]
