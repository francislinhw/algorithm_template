# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from typing import List
from collections import deque

# def solution(grid):
# 	if not grid:
#   	retrun -1
# 	if grid[0][0] == 1:
#   	return -1

#   queue = deque([])

#   queue.append([0, 0])

#   target = [len(grid[0] - 1), len(grid) - 1] #x, y
#   visited = set()

#   step = 1

#   directions = [[0, -1], [0, 1], [1, 0], [-1, 0], [-1, -1], [1, -1], [-1, 1], [1, 1]]

#   while queue != []:
#   	currentElements = queue.popleft()
#     step += 1

#     for element in currentElements:
#     	if element not in visited and element[0] > 0 and element[1] > 0 and element[0] < len(grid[0]) and element[1] < len(grid) and grid[element[0]][element[1]] != 1:
#     		visited.add(element)
#         if element == target:
#           return step
#         else:
#           for direction in directions:
# 						allDirections.append(element + direction) # visuli
#           	if element not in visited and element[0] > 0 and element[1] > 0 and element[0] < len(grid[0]) and element[1] < len(grid) and grid[element[0]][element[1]] != 1:
#         			queue.append(direction)

#   return -1

#   # time complexiyt: O(m * n) => 8 * m * n
#   # space comlexity: O(m * n)


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        q = deque([(0, 0, 1)])
        visit = set((0, 0))
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while q:
            r, c, length = q.popleft()
            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in direct:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < N
                    and 0 <= nc < N
                    and grid[nr][nc] == 0
                    and (nr, nc) not in visit
                ):
                    q.append((nr, nc, length + 1))
                    visit.add((nr, nc))

        return -1
