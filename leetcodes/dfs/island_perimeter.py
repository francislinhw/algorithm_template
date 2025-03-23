# https://leetcode.com/problems/island-perimeter/

from typing import List

# 23 March 2025


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 12.46

        # Step 1: Find one part of the island
        # Step 2: DFS iterate the island and also count the perimeter
        xLen = len(grid[0])
        yLen = len(grid)

        perimeter = [0]

        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if (x, y) in visited or x < 0 or y < 0 or x >= xLen or y >= yLen:
                return
            if grid[y][x] == 0:
                return
            visited.add((x, y))

            for dx, dy in directions:
                neighborX = x + dx
                neighborY = y + dy
                if (
                    neighborX < 0
                    or neighborY < 0
                    or neighborX >= xLen
                    or neighborY >= yLen
                ):
                    perimeter[0] += 1
                elif grid[neighborY][neighborX] == 0:
                    perimeter[0] += 1
                else:
                    perimeter[0] += 0

            for dx, dy in directions:
                dfs(x + dx, y + dy)

        for i in range(xLen):
            for j in range(yLen):
                if grid[j][i] == 1 and (i, j) not in visited:
                    dfs(i, j)

        return perimeter[0]  # 20 Mins


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        # r * c
        rGrid = len(grid)
        cGrid = len(grid[0])

        visitedSet = set()

        def isSeaOrEdge(r, c):
            if (r, c) in visitedSet:
                return False
            if r < 0 or r >= rGrid or c < 0 or c >= cGrid or grid[r][c] == 0:
                return True

        def countingPerimeter(r, c):
            if (
                (r, c) in visitedSet
                or r < 0
                or r >= rGrid
                or c < 0
                or c >= cGrid
                or grid[r][c] == 0
            ):
                return 0

            visitedSet.add((r, c))

            side = 0
            side += 1 if isSeaOrEdge(r, c - 1) == True else 0
            side += 1 if isSeaOrEdge(r, c + 1) == True else 0
            side += 1 if isSeaOrEdge(r - 1, c) == True else 0
            side += 1 if isSeaOrEdge(r + 1, c) == True else 0

            upper = countingPerimeter(r, c - 1)
            lower = countingPerimeter(r, c + 1)
            left = countingPerimeter(r - 1, c)
            right = countingPerimeter(r + 1, c)

            return side + upper + lower + left + right

        perimeter = 0

        for r in range(rGrid):
            for c in range(cGrid):
                if (r, c) in visitedSet:
                    continue

                perimeter += countingPerimeter(r, c)

        return perimeter


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        visited = set()
        rowLen = len(grid)
        colLen = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rowLen or c >= colLen or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            top = dfs(r - 1, c)
            down = dfs(r + 1, c)
            right = dfs(r, c + 1)
            left = dfs(r, c - 1)
            return top + down + left + right

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    return dfs(i, j)
