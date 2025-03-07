# https://leetcode.com/problems/rotate-image/

from typing import List


# correct


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        # 3.52
        # Step 1 find a way to modify blocks: My finding is move 2 clockwise
        blockToModify = [(0, 0), matrix[0][0]]

        def findNewXY(x, y):
            return n - y, x

        for i in range(n):
            for j in range(n):
                x, y = blockToModify[0]
                thisBlockValue = blockToModify[1]
                newX, newY = findNewXY(x, y)
                print("newX", newX)
                print("newY", newY)
                valueToBeTakenOut = matrix[newY][newX]
                matrix[newY][newX] = thisBlockValue
                blockToModify = [(newX, newY), valueToBeTakenOut]

        return matrix
        # 4.31止損


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix[0]) - 1

        while r > l:
            for i in range(r - l):
                t = l
                b = r
                topLeft = matrix[t][l + i]  # Top Left
                matrix[t][l + i] = matrix[b - i][l]  # Left Down
                matrix[b - i][l] = matrix[b][r - i]  #
                matrix[b][r - i] = matrix[t + i][r]  # Top Right
                matrix[t + i][r] = topLeft  # Top Right
            l += 1
            r -= 1
        return matrix
