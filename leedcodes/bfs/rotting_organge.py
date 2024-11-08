from collections import deque
from typing import List


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
                    if (newR < 0 or newC < 0 or newR >= rows or newC >= cols or 
                        (newR, newC) in visited or grid[newR][newC] == 0 or grid[newR][newC] == 2):
                        continue
                    visited.add((newR,newC))
                    q.append((newR, newC))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1