# https://leetcode.com/problems/spiral-matrix/


# 4 March 2025 Practice
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 9.56
        height = len(matrix)
        width = len(matrix[0])

        blocks = int(height * width)

        visited = set()

        result = []

        w = 0
        h = 0

        direction = "right"  # "down" "up" "left"

        for i in range(blocks):
            if direction == "right" and (w > width - 1 or (w, h) in visited):
                w = w - 1
                h += 1
                direction = "down"
            elif direction == "down" and (h > height - 1 or (w, h) in visited):
                h = h - 1
                w -= 1
                direction = "left"
            elif direction == "left" and (w < 0 or (w, h) in visited):
                w += 1
                h -= 1
                direction = "up"
            elif direction == "up" and (h < 0 or (w, h) in visited):
                w += 1
                h += 1
                direction = "right"

            visited.add((w, h))
            result.append(matrix[h][w])

            if direction == "right":
                w += 1
            elif direction == "down":
                h += 1
            elif direction == "up":
                h -= 1
            elif direction == "left":
                w -= 1

        return result  # 10.24


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
