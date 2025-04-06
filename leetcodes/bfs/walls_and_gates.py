from typing import (
    List,
)
from collections import deque


# https://www.lintcode.com/problem/663/description

from typing import (
    List,
)

from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        # 3.00
        if not rooms or not rooms[0]:
            return

        xLen = len(rooms[0])
        yLen = len(rooms)

        ROOM = 2147483647
        GATE = 0
        BLOCK = -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            visited = set()
            layer = 0

            while queue:
                for _ in range(len(queue)):
                    cX, cY = queue.popleft()
                    if (cX, cY) in visited:
                        continue
                    visited.add((cX, cY))

                    if rooms[cY][cX] == GATE:
                        return layer
                    if rooms[cY][cX] == BLOCK:
                        continue

                    for dx, dy in directions:
                        nx, ny = cX + dx, cY + dy
                        if 0 <= nx < xLen and 0 <= ny < yLen and (nx, ny) not in visited:
                            queue.append((nx, ny))
                layer += 1

            return None  # No gate found

        for y in range(yLen):
            for x in range(xLen):
                if rooms[y][x] == ROOM:
                    step = bfs(x, y)
                    if step is not None:
                        rooms[y][x] = step
        # What is the case if there is no way to reach the gate for a room?


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
