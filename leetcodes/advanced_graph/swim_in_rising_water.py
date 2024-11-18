# https://leetcode.com/problems/swim-in-rising-water/
from typing import List
from collections import heapq


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
