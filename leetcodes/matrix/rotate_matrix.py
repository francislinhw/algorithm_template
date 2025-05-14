# https://leetcode.com/problems/rotate-image/description/


class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # 外層圈數，只要處理一半（上下對稱）
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                # 存暫存值
                temp = matrix[i][j]

                # 進行四個角的輪換（順時針）
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp

        return matrix


class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

        return matrix
