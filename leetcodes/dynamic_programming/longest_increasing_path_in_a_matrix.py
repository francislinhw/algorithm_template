from typing import List


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # 10.52
        # DFS -> TLE
        # DP -> Map
        if not matrix or not matrix[0]:
            return 0

        y, x = len(matrix), len(matrix[0])
        dp = [[1 for _ in range(x)] for _ in range(y)]
        cells = []

        for i in range(y):
            for j in range(x):
                cells.append((matrix[i][j], i, j))

        # 按照 matrix 的值從小排到大
        cells.sort()

        # 四個方向
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for value, i, j in cells:
            for dy, dx in directions:
                ni, nj = i + dy, j + dx
                if 0 <= ni < y and 0 <= nj < x and matrix[ni][nj] > value:
                    dp[ni][nj] = max(dp[ni][nj], dp[i][j] + 1)

        # 回傳整張 dp 裡的最大值
        return max(max(row) for row in dp)


from collections import deque


class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        indegree = [[0] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Step 1: 建立每個節點的 in-degree
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and matrix[nr][nc] > matrix[r][c]
                    ):
                        indegree[nr][nc] += 1  # 增加入度表示有個節點指向它

        # Step 2: 把所有入度為 0 的格子放入 queue
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if indegree[r][c] == 0:
                    queue.append((r, c))

        # Step 3: 拓撲排序（每一層就是一個遞增長度）
        longest_path = 0
        while queue:
            longest_path += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and matrix[nr][nc] > matrix[r][c]
                    ):
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            queue.append((nr, nc))

        return longest_path


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        res = 0
        seem = {}

        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0

            if (i, j) in seem:
                return seem[(i, j)]
            up = 1 + dfs(i - 1, j, matrix[i][j])
            down = 1 + dfs(i + 1, j, matrix[i][j])
            left = 1 + dfs(i, j - 1, matrix[i][j])
            right = 1 + dfs(i, j + 1, matrix[i][j])
            total = max(up, down, left, right)
            seem[(i, j)] = total

            return seem[(i, j)]

        for i in range(m):
            for j in range(n):
                temp = dfs(i, j, -1)
                res = max(res, temp)

        return res


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]

            max_len = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

            memo[r][c] = max_len
            return max_len

        return max(dfs(r, c) for r in range(rows) for c in range(cols))
