from typing import List


class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []

        rLen = len(heights)
        cLen = len(heights[0])

        pacificReachable = set()
        atlanticReachable = set()

        def dfs(r, c, reachableSet, prevHeight):
            if (
                (r, c) in reachableSet
                or r < 0
                or r >= rLen
                or c < 0
                or c >= cLen
                or heights[r][c] < prevHeight
            ):
                return None

            reachableSet.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, reachableSet, heights[r][c])


# https://leetcode.com/problems/pacific-atlantic-water-flow/
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pVisited = set()
        aVisited = set()

        res = []

        def dfs(r, c, visited, prevVal):
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or heights[r][c] < prevVal
                or (r, c) in visited
            ):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pVisited, heights[0][c])
            dfs(rows - 1, c, aVisited, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pVisited, heights[r][0])
            dfs(r, cols - 1, aVisited, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pVisited and (r, c) in aVisited:
                    res.append([r, c])
        return res
