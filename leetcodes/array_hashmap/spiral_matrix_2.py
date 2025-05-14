# https://leetcode.com/problems/spiral-matrix-ii/description/


class Solution(object):
    def generateMatrix(self, n):
        shape = [[0 for _ in range(n)] for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
        dir_idx = 0
        x, y = 0, 0

        for count in range(1, n * n + 1):
            shape[x][y] = count
            # 預測下一步
            nx = x + directions[dir_idx][0]
            ny = y + directions[dir_idx][1]
            # 若出界或已填過就轉向
            if nx < 0 or nx >= n or ny < 0 or ny >= n or shape[nx][ny] != 0:
                dir_idx = (dir_idx + 1) % 4
                nx = x + directions[dir_idx][0]
                ny = y + directions[dir_idx][1]
            x, y = nx, ny

        return shape
