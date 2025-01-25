# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1

        while l < r and t < b:
            for i in range(l, r):
                res.append(matrix[t][i])
            for j in range(t, b):
                res.append(matrix[j][r])
            for k in reversed(range(l + 1, r + 1)):
                res.append(matrix[b][k])
            for z in reversed(range(t + 1, b + 1)):
                res.append(matrix[z][l])
            l += 1
            r -= 1
            t += 1
            b -= 1
        # 扁的長方形
        if t == b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
        # 正方形
        if t == b and l == r:
            return res
        # 高的長方形
        if l == r:
            for j in range(t, b + 1):
                res.append(matrix[j][l])
        return res
        # homework robot way
