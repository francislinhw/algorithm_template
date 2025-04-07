# https://leetcode.com/problems/swim-in-rising-water/
from typing import List
from collections import heapq

import heapq


class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  # (max_so_far, x, y)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while heap:
            height, x, y = heapq.heappop(heap)
            if x == n - 1 and y == n - 1:
                return height
            if visited[y][x]:
                continue
            visited[y][x] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                    heapq.heappush(heap, (max(height, grid[ny][nx]), nx, ny))


class Solution(object):
    def swimInWater(self, grid):
        visited = set()
        xLen = len(grid[0])
        yLen = len(grid)
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, path):
            if x == (xLen - 1) and y == (yLen - 1):
                path.append(grid[y][x])
                res.append(path[:])
                path.pop()
                return
            visited.add((x, y))
            path.append(grid[y][x])
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < xLen and 0 <= ny < yLen and (nx, ny) not in visited:
                    dfs(nx, ny, path)
            path.pop()
            visited.remove((x, y))

        dfs(0, 0, [])
        minInPath = float("inf")
        for path in res:
            maxValue = max(path)
            minInPath = min(maxValue, minInPath)
        return minInPath


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 2D 題目, 用模板
        # bfs (with heap)

        rowLen = len(grid)
        colLen = len(grid[0])
        visited = set()

        h = [(grid[0][0], 0, 0)]  # (height, r, c)
        heapq.heapify(h)

        while h:
            height, row, col = heapq.heappop(h)
            if (row, col) in visited:
                continue

            if row == rowLen - 1 and col == colLen - 1:
                return height

            # hight = max(hight, )
            visited.add((row, col))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR = row + dr
                newC = col + dc
                if (
                    newR < 0
                    or newR >= rowLen
                    or newC < 0
                    or newC >= colLen
                    or (newR, newC) in visited
                ):
                    continue
                heapq.heappush(h, (max(grid[newR][newC], height), newR, newC))


def swimInRisingWater(grid: List[List[int]]) -> int:
    heap = []
    heapq.heapify(heap)
    heapq.heappush([grid[0][0], 0, 0])

    visited = set()
    count = 1

    while heap:
        hight, col, row = heapq.popleft(heap)

        if (col, row) in visited:
            continue

        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return count

        for dh, dv in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newRow = row + dv
            newCol = col + dh

            if (
                newRow >= len(grid)
                or newCol >= len(grid[0])
                or newRow < 0
                or newCol < 0
                or (newCol, newRow) in visited
            ):
                continue

            newHight = grid[newCol][newRow]
            count += 1
            heapq.heappush(heap, [newHight, newCol, newRow])

    return count
