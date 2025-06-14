# https://leetcode.com/problems/max-area-of-island/
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 10.55
        if not grid:
            return 0
        xLen, yLen = len(grid[0]), len(grid)

        visited = set()
        maxArea = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = []

        def dfs(x, y):
            if (
                (x, y) in visited
                or x < 0
                or y < 0
                or x > xLen - 1
                or y > yLen - 1
                or grid[y][x] == 0
            ):
                return 0
            visited.add((x, y))
            if (x, y) not in area:
                area.append((x, y))

            for dx, dy in directions:
                dfs(dx + x, dy + y)

        for i in range(xLen):
            for j in range(yLen):
                if (i, j) not in visited:
                    area = []
                    dfs(i, j)
                maxArea = max(maxArea, len(area))

        return maxArea  # 13 min


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
