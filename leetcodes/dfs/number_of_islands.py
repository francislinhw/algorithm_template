# https://leetcode.com/problems/number-of-islands/description/
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 12.11
        xLen, yLen = len(grid[0]), len((grid))

        visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        count = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x > xLen - 1 or y > yLen - 1:
                return False
            if grid[y][x] == "0":
                return False
            if (x, y) in visited:
                return
            visited.add((x, y))

            for dx, dy in directions:
                dfs(x + dx, y + dy)
            return True

        for i in range(xLen):
            for j in range(yLen):
                if dfs(i, j):
                    count += 1

        return count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 3/22 4.37
        # Use DFS to find whole island and cnt it
        # For loop to iterate whole graph

        if not grid:
            return 0

        visited = set()

        xLen = len(grid[0])
        yLen = len(grid)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if (x, y) in visited or x < 0 or y < 0 or x >= xLen or y >= yLen:
                return
            if grid[y][x] == "0":
                return
            visited.add((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        numberOfIsland = 0

        for i in range(xLen):
            for j in range(yLen):
                if (i, j) not in visited and grid[j][i] == "1":
                    numberOfIsland += 1
                    dfs(i, j)

        return numberOfIsland  # 10 min


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 3/22 4.37
        # Use DFS to find whole island and cnt it
        # For loop to iterate whole graph

        if not grid:
            return 0

        visited = set()

        xLen = len(grid[0])
        yLen = len(grid)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if (x, y) in visited or x < 0 or y < 0 or x >= xLen or y >= yLen:
                return
            if grid[y][x] == "0":
                return
            visited.add((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        numberOfIsland = 0

        for i in range(xLen):
            for j in range(yLen):
                if (i, j) not in visited and grid[j][i] == "1":
                    numberOfIsland += 1
                    dfs(i, j)

        return numberOfIsland  # 10 min


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or grid[r][c] == "0"
                or (r, c) in visited
            ):
                return False

            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

            return True

        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited or grid[r][c] == "0":
                    continue
                if dfs(r, c):
                    count += 1
        return count


# example
input = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

expected_output = 1

s = Solution()
print(s.numIslands(input) == expected_output)
