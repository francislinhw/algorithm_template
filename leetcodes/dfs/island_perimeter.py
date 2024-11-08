# https://leetcode.com/problems/island-perimeter/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0
        
        # r * c
        rGrid = len(grid)
        cGrid = len(grid[0])

        visitedSet = set()

        def isSeaOrEdge(r, c):
            if (r, c) in visitedSet:
                return False
            if r < 0 or r >= rGrid or c < 0 or c >= cGrid or grid[r][c] == 0:
                return True


        def countingPerimeter(r, c):
            if (r, c) in visitedSet or r < 0 or r >= rGrid or c < 0 or c >= cGrid or grid[r][c] == 0:
                return 0
            
            visitedSet.add((r, c))

            side = 0
            side += 1 if isSeaOrEdge(r, c-1) == True else 0
            side += 1 if isSeaOrEdge(r, c+1) == True else 0
            side += 1 if isSeaOrEdge(r-1, c) == True else 0
            side += 1 if isSeaOrEdge(r+1, c) == True else 0

            upper = countingPerimeter(r, c-1)
            lower = countingPerimeter(r, c+1)
            left = countingPerimeter(r-1, c)
            right = countingPerimeter(r+1, c)

            return side + upper + lower + left + right
        
        perimeter = 0

        for r in range(rGrid):
            for c in range(cGrid):
                if (r, c) in visitedSet:
                    continue
                
                perimeter += countingPerimeter(r, c)

        return perimeter


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        visited = set()
        rowLen = len(grid)
        colLen = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rowLen or c >= colLen or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            top = dfs(r-1, c)
            down = dfs(r+1, c)
            right = dfs(r, c+1)
            left = dfs(r, c-1)
            return top + down + left + right



        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    return dfs(i, j)