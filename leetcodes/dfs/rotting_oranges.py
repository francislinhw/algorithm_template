# https://leetcode.com/problems/rotting-oranges/

from typing import List
from collections import deque


# 21 Mar 2025 Practice
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        xLen, yLen = len(grid[0]), len(grid)
        visited = set()
        queue = deque()

        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == 2:
                    visited.add((x, y))
                    queue.append((x, y))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rottenRound = 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < xLen
                        and 0 <= ny < yLen
                        and grid[ny][nx] == 1
                        and (nx, ny) not in visited
                    ):
                        grid[ny][nx] = 2
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            if queue:  # Only increment if there's another layer to process
                rottenRound += 1

        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == 1:
                    return -1

        return rottenRound
