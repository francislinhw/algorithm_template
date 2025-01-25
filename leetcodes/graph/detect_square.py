# https://leetcode.com/problems/detect-squares/

from typing import List


class DetectSquares:

    def __init__(self):
        points = {}

    def add(self, point: List[int]) -> None:
        points = (point[0], point[1])
        if points not in self.ptsCnt:
            self.ptsCnt[points] = 1
            return
        self.ptsCnt[points] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        for px, py in self.ptsCnt:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            if (px, y) in self.ptsCnt and (x, py) in self.ptsCnt:
                res += self.ptsCnt[(px, y)] * self.ptsCnt[(x, py)] * self.ptsCnt[(px, py)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
