# https://leetcode.com/problems/rotting-oranges/description/
from collections import deque
from typing import List

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return -1

        yLen, xLen = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rottonSet = set()
        freshSet = set()

        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == 1:
                    freshSet.add((x, y))
                elif grid[y][x] == 2:
                    rottonSet.add((x, y))

        q = deque(rottonSet)
        layer = 0

        while q and freshSet:
            layer += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in freshSet:
                        freshSet.remove((nx, ny))
                        q.append((nx, ny))

        return -1 if freshSet else layer


# 4 Apr 2025 practice
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 12.01
        # BFS layer by layer
        # check if there are 1 inside it.
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Initialize queue with rotten oranges and count fresh ones
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        step = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
            step += 1

        return step - 1 if fresh == 0 else -1


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc
                    if (
                        newR < 0
                        or newC < 0
                        or newR >= rows
                        or newC >= cols
                        or (newR, newC) in visited
                        or grid[newR][newC] == 0
                        or grid[newR][newC] == 2
                    ):
                        continue
                    visited.add((newR, newC))
                    q.append((newR, newC))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
