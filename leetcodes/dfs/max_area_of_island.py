# https://leetcode.com/problems/max-area-of-island/
from typing import List


# 3/22 4.37 2025
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 3/22 4.37
        # Use DFS to find whole island and cnt it
        # For loop to iterate whole graph

        if not grid:
            return 0

        visited = set()

        xLen = len(grid[0])
        yLen = len(grid)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        maxArea = 0

        def dfs(x, y):
            if (
                (x, y) in visited
                or x < 0
                or y < 0
                or x >= xLen
                or y >= yLen
                or grid[y][x] == 0
            ):
                return 0
            visited.add((x, y))
            area = 1
            for dx, dy in directions:
                area += dfs(x + dx, y + dy)
            return area

        # 然後在主程式裡：
        maxArea = 0
        for y in range(yLen):
            for x in range(xLen):
                if (x, y) not in visited and grid[y][x] == 1:
                    maxArea = max(maxArea, dfs(x, y))

        return maxArea  # 10 min
