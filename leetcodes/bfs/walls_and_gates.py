from typing import (
    List,
)
from collections import deque


# https://www.lintcode.com/problem/663/description
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, grid: List[List[int]]):
        # write your code here
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rowLen = len(grid)
        colLen = len(grid[0])

        visited = set()

        q = deque()  # only diff of bfs dfs

        # add gates
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 0:
                    q.append((r, c))

        count = 0  # bfs
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                if grid[r][c] > 0:
                    grid[r][c] = count
                # go 4 directions
                for dr, dc in direction:
                    newR = r + dr
                    newC = c + dc
                    if (
                        newR < 0
                        or newC < 0
                        or newR >= rowLen
                        or newC >= colLen
                        or grid[newR][newC] <= 0
                        or (newR, newC) in visited
                    ):
                        continue
                    q.append((newR, newC))
            count += 1
        return grid


# Test Cases

input = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]

s = Solution()


print(s.walls_and_gates(input) == expected)
