# https://leetcode.com/problems/count-sub-islands/
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """

        if not grid1 or not grid2:
            return 0
        
        rLen = len(grid1)
        cLen = len(grid1[0])

        subGrid = [0] * rLen

        for r in range(rLen):
            subGrid[r] = [0] * cLen
        

        for r in range(rLen):
            for c in range(cLen):
                subGrid[r][c] = 1 if grid1[r][c] == 1 and grid2[r][c] == 1 else 0
        
        numberIsland = 0

        visitedSet = set()

        def visitWholeIsland(r, c):
            if (r, c) in visitedSet or r < 0 or r >= rLen or c < 0 or c >= cLen or subGrid[r][c] == 0:
                return False

            visitedSet.add((r, c))

            visitWholeIsland(r+1, c)
            visitWholeIsland(r, c+1)
            visitWholeIsland(r-1, c)
            visitWholeIsland(r, c-1)

            return True
        
        for r in range(rLen):
            for c in range(cLen):
                if (r, c) in visitedSet:
                    continue
                if visitWholeIsland(r, c):
                    numberIsland += 1
        
        return numberIsland
    
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
expected = 3

s = Solution()
a = s.countSubIslands(grid1, grid2)
print(a == expected, a)
