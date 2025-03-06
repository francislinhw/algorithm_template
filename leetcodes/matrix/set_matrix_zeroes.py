# https://leetcode.com/problems/set-matrix-zeroes/description/

from typing import List


# 4 March 2025
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 10.50

        auxilaryRow = [False for i in range(len(matrix))]
        auxilaryColumn = [False for i in range(len(matrix[0]))]

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i] == 0:
                    auxilaryRow[j] = True
                    auxilaryColumn[i] = True

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if auxilaryRow[j] == True:
                    matrix[j][i] = 0
                if auxilaryColumn[i] == True:
                    matrix[j][i] = 0

        return matrix  # 8 min


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1) complexity
        # O(n) -> O(1) Space

        rows = len(matrix)
        cols = len(matrix[0])
        rowZero = False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        rowZero = True
                    else:
                        matrix[i][0] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        for j in range(cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
        if rowZero:
            for j in range(cols):
                matrix[0][j] = 0

        return matrix
