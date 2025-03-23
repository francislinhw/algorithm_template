# https://leetcode.com/problems/count-sub-islands/
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # 1.45 # Bad
        # Step 1: Iterate Grid 1 and have visted
        # Step 2: Iterate Grid 2 and have isolated island
        # Step 3: Check if the island in the grid2 is all in grid 1

        xLen = len(grid1[0])
        yLen = len(grid1)

        visited = set()
        visitedg2 = set()
        visitedForLoop = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if (x, y) in visited or x < 0 or y < 0 or x >= xLen or y >= yLen:
                return
            if grid1[y][x] == 0:
                return
            visited.add((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        for i in range(xLen):
            for j in range(yLen):
                if (i, j) not in visited and grid1[j][i] == 1:
                    dfs(i, j)

        def dfsg2(x, y):
            if (x, y) in visitedForLoop or x < 0 or y < 0 or x >= xLen or y >= yLen:
                return
            if grid2[y][x] == 0:
                return
            visitedg2.add((x, y))
            visitedForLoop.add((x, y))
            for dx, dy in directions:
                dfsg2(x + dx, y + dy)

        grid2Islands = []

        for i in range(xLen):
            for j in range(yLen):
                if (i, j) not in visitedForLoop and grid2[j][i] == 1:
                    dfsg2(i, j)
                    grid2Islands.append(list(visitedg2))
                    visitedg2 = set()

        result = 0

        for island in grid2Islands:
            isAllIn = True
            for isld in island:
                if isld not in list(visited):
                    isAllIn = False
            if isAllIn:
                result += 1

        return result

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        yLen, xLen = len(grid1), len(grid1[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(x, y):
            if (x, y) in visited or x < 0 or y < 0 or x >= xLen or y >= yLen:
                return True
            if grid2[y][x] == 0:
                return True  # 不影響 sub-island 判斷

            visited.add((x, y))

            # 只要 grid2 是陸地，但 grid1 是水，那就不是 sub-island
            is_sub = grid1[y][x] == 1

            for dx, dy in directions:
                is_sub = dfs(x + dx, y + dy) and is_sub  # 必須所有子點都合法

            return is_sub

        count = 0
        for y in range(yLen):
            for x in range(xLen):
                if grid2[y][x] == 1 and (x, y) not in visited:
                    if dfs(x, y):
                        count += 1

        return count


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
            if (
                (r, c) in visitedSet
                or r < 0
                or r >= rLen
                or c < 0
                or c >= cLen
                or subGrid[r][c] == 0
            ):
                return False

            visitedSet.add((r, c))

            visitWholeIsland(r + 1, c)
            visitWholeIsland(r, c + 1)
            visitWholeIsland(r - 1, c)
            visitWholeIsland(r, c - 1)

            return True

        for r in range(rLen):
            for c in range(cLen):
                if (r, c) in visitedSet:
                    continue
                if visitWholeIsland(r, c):
                    numberIsland += 1

        return numberIsland


grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
]
expected = 3

s = Solution()
a = s.countSubIslands(grid1, grid2)
print(a == expected, a)
