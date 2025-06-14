from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificVisited = set()
        atlanticVisited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, prevHeight, visited):
            if (x, y) in visited:
                return
            if y < 0 or x < 0 or y >= len(heights) or x >= len(heights[0]):
                return

            curHeight = heights[y][x]
            if curHeight < prevHeight:
                return

            visited.add((x, y))

            for dx, dy in directions:
                dfs(x + dx, y + dy, curHeight, visited)

        rows, cols = len(heights), len(heights[0])

        for y in range(rows):
            dfs(0, y, heights[y][0], pacificVisited)  # 左邊界
            dfs(cols - 1, y, heights[y][cols - 1], atlanticVisited)  # 右邊界

        for x in range(cols):
            dfs(x, 0, heights[0][x], pacificVisited)  # 上邊界
            dfs(x, rows - 1, heights[rows - 1][x], atlanticVisited)  # 下邊界

        res = []
        for x, y in pacificVisited & atlanticVisited:
            res.append([y, x])  # 注意：output 要 [row, col]

        return res


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 3.20
        # Step1: DFS Problem - For loop each cells
        # Step2: DFS to identify if the cell is connect to Pacific/Altantic
        # Step3: Return My findings

        # Base
        if not heights or not heights[0]:
            return []

        yLen, xLen = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []

        def dfs(x, y, visited):
            if (x, y) in visited:
                return False, False

            visited.add((x, y))
            pacific = x == 0 or y == 0
            atlantic = x == xLen - 1 or y == yLen - 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < xLen and 0 <= ny < yLen and heights[ny][nx] <= heights[y][x]:
                    p, a = dfs(nx, ny, visited)
                    pacific = pacific or p
                    atlantic = atlantic or a

            return pacific, atlantic

        for y in range(yLen):
            for x in range(xLen):
                visited = set()
                pac, atl = dfs(x, y, visited)
                if pac and atl:
                    result.append([y, x])

        return result


# 22 Mar 2025 Practice
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        yLen, xLen = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []

        def dfs(x, y, visited):
            if (x, y) in visited:  # Already start without new cell
                return False, False

            visited.add((x, y))
            pacific = x == 0 or y == 0
            atlantic = x == xLen - 1 or y == yLen - 1

            # DFS will go all the way to the edge of the map
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < xLen and 0 <= ny < yLen and heights[ny][nx] <= heights[y][x]:
                    p, a = dfs(nx, ny, visited)
                    pacific = pacific or p
                    atlantic = atlantic or a

            # After DFS, it knows if the cell is connect to Pacific/Atlantic
            return pacific, atlantic

        for y in range(yLen):
            for x in range(xLen):
                visited = set()
                pac, atl = dfs(x, y, visited)
                if pac and atl:
                    result.append([y, x])

        return result


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        yLen, xLen = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, visited, prevHeight):
            if (
                x < 0
                or x >= xLen
                or y < 0
                or y >= yLen
                or (x, y) in visited
                or heights[y][x] < prevHeight
            ):
                return
            visited.add((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy, visited, heights[y][x])

        result = []

        for y in range(yLen):
            for x in range(xLen):
                pacific_visited = set()
                atlantic_visited = set()

                dfs(x, y, pacific_visited, heights[y][x])
                dfs(x, y, atlantic_visited, heights[y][x])

                # 如果這個點的水流可以觸碰到 Pacific 和 Atlantic
                if any(px == 0 or py == 0 for (px, py) in pacific_visited) and any(
                    px == xLen - 1 or py == yLen - 1 for (px, py) in atlantic_visited
                ):
                    result.append([y, x])

        return result


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 3.20
        # Step1: DFS Problem - For loop each cells
        # Step2: DFS to identify if the cell is connect to Pacific/Altantic
        # Step3: Return My findings

        # Base
        if not heights:
            return []

        yLen = len(heights)
        xLen = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, visited, prevHeight):
            if (
                x < 0
                or x >= xLen
                or y < 0
                or y >= yLen
                or (x, y) in visited
                or heights[y][x] < prevHeight
            ):
                return
            visited.add((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy, visited, heights[y][x])

        # 從 Pacific 的邊界開始 DFS
        for i in range(xLen):
            dfs(i, 0, pacific, heights[0][i])  # 上邊界
            dfs(i, yLen - 1, atlantic, heights[yLen - 1][i])  # 下邊界
        for j in range(yLen):
            dfs(0, j, pacific, heights[j][0])  # 左邊界
            dfs(xLen - 1, j, atlantic, heights[j][xLen - 1])  # 右邊界

        result = []
        for y in range(yLen):
            for x in range(xLen):
                if (x, y) in pacific and (x, y) in atlantic:
                    result.append([y, x])

        return result


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
