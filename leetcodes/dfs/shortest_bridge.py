# https://leetcode.com/problems/shortest-bridge/description/

# Time: O(n^2)
from collections import deque
from typing import List


# 21 Mar 2025 Practice
class Solution(object):
    def shortestBridge(self, grid):
        xLen = len(grid[0])
        yLen = len(grid)
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque()

        # Find first island
        def dfs(x, y):
            if (
                x < 0
                or x >= xLen
                or y < 0
                or y >= yLen
                or (x, y) in visited
                or grid[y][x] != 1
            ):
                return
            visited.add((x, y))
            queue.append((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        found = False
        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == 1:
                    dfs(x, y)
                    found = True
                    break
            if found:
                break

        # BFS to find shortest path to the second island
        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < xLen and 0 <= ny < yLen and (nx, ny) not in visited:
                        if grid[ny][nx] == 1:
                            return steps
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            steps += 1

        return -1  # in case something is wrong


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N

        visit = set()

        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0, deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append((curR, curC))
                        visit.add((curR, curC))
                res += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c]:  # land will run
                    dfs(r, c)
                    return bfs()


"""

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [ [1,1,1,1,1],
								[1,0,0,0,1],
								[1,0,1,0,1],
								[1,0,0,0,1],
								[1,1,1,1,1]]
Output: 1


# 1. Step: For iterate the grid to find the first 1,

# 2. Step: Write a DFS Function find the whole entity

# 3. Step: BFS to find another island layer by layer # Hint: take one island as entity and expand it


def function(grid):
	if not grid:
  	return 0
  
  yLen = len(grid)
  xLen = len(grid[0])
    
  x, y = 0, 0  
    
  for i in range(xLen):
  	for j in range(yLen):
    	if grid[i][j] != 0:
      	x, y = i, j
      	break
  
  visited = set()
  # entity = [(x, y), (x1, y1)]
  # Hint 
  nextLayer = set()
  
	def dfs(x, y):
  	if x < 0 or y < 0 or x >= xLen or y >= yLen or (x, y) in visited:
    	continue
  	if grid[x][y] == 0:
    	nextLayer.append((x, y))
    visited.append((x, y))
    dfs(x + 1, y)
    dfs(x, y + 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    
  dfs(x, y)
  
  q = deque([visited])
  numberOfLayer = 0
  
  while q:
  	x, y = q.popleft()
    
    for 
    
  
  -----------------------------------------

	
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N

        visit = set()

        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0, deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append((curR, curC))
                        visit.add((curR, curC))
                res += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()
	
  
  
"""
