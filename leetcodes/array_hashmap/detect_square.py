# https://leetcode.com/problems/detect-squares/

from typing import List
from collections import defaultdict


# 5 Apr 2025 practice
class DetectSquares:

    def __init__(self):
        self.point_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (px, py), cnt in self.point_count.items():
            # 忽略不是對角線的點
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue

            # 形成正方形的另外兩個點
            if (px, y) in self.point_count and (x, py) in self.point_count:
                total += cnt * self.point_count[(px, y)] * self.point_count[(x, py)]

        return total


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


class DetectSquares(object):
    def __init__(self):
        self.cntMap = {}  # 記錄點的數量

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        if tuple(point) not in self.cntMap:
            self.cntMap[tuple(point)] = 0
        self.cntMap[tuple(point)] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x1, y1 = point
        cnt = 0

        # 遍歷 `cntMap.keys()`，只選擇 (x2, y2) 為 `point` 的對角點
        for x2, y2 in self.cntMap.keys():
            if abs(x1 - x2) != abs(y1 - y2) or x1 == x2 or y1 == y2:
                continue  # 必須是對角線上的點

            # 計算剩下兩個頂點
            p3 = (x1, y2)
            p4 = (x2, y1)

            # 確保 `p3, p4` 存在於 `cntMap`
            if p3 in self.cntMap and p4 in self.cntMap:
                cnt += self.cntMap[(x2, y2)] * self.cntMap[p3] * self.cntMap[p4]

        return cnt


# 16 March 2025
class DetectSquares(object):
    # 9.30

    def __init__(self):
        self.points = []
        self.cntMap = {}

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.points.append(point)
        if tuple(point) not in self.cntMap:
            self.cntMap[tuple(point)] = 0
        self.cntMap[tuple(point)] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        # Step1: Define a algo to pick the diagnals point from slected point
        diagonals = []
        for originalPoints in self.points:
            diagonals.append([point, originalPoints])

        # Step2: Generate two others points from diagonal (also filter)
        cnt = 0
        for p1, p2 in diagonals:
            if p1 == p2:  # zero square
                continue

            if abs(p1[0] - p2[0]) != abs(p1[1] - p2[1]):
                continue

            p3 = [p1[0], p2[1]]
            p4 = [p2[0], p1[1]]
            if tuple(p3) in self.cntMap and tuple(p4) in self.cntMap:

                cnt += 1 * self.cntMap[tuple(p3)] * self.cntMap[tuple(p4)]

        return cnt


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
