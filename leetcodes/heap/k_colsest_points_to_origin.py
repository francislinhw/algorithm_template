import heapq
from math import sqrt


# https://leetcode.com/problems/k-closest-points-to-origin/description/

import random


class Solution(object):
    def kClosest(self, points, k):
        # 7.11
        pathOrder = []
        lengthMap = {}

        for x, y in points:
            distance = x**2 + y**2
            if distance not in lengthMap:
                pathOrder.append(distance)
                lengthMap[distance] = []
            lengthMap[distance].append([x, y])

        # Quickselect
        def quickSearch(arr, k):
            if not arr:
                return None

            pivot = random.choice(arr)
            pivots = [n for n in arr if n == pivot]
            less = [n for n in arr if n < pivot]
            greater = [n for n in arr if n > pivot]

            if k < len(less):
                return quickSearch(less, k)
            elif k < len(less) + len(pivots):
                return pivot
            else:
                return quickSearch(greater, k - len(less) - len(pivots))

        target_dist = quickSearch(pathOrder, k - 1)

        result = []
        for d in sorted(lengthMap):
            result += lengthMap[d]
            if len(result) >= k:
                return result[:k]

        return result  # backup 26 min


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if not points:
            return []

        listSD = []  # index length

        def lenToOrigin(x, y):
            return sqrt(x**2 + y**2)

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            # all sort by default is by index 0
            listSD.append([lenToOrigin(x, y), x, y])

        heapq.heapify(listSD)  # O(n)

        returnList = []

        for i in range(k):
            distance, x, y = heapq.heappop(listSD)
            returnList.append([x, y])

        return returnList

        # list1.sort(key = ) Check
        # BigO(O(n) + O(n) + O(k * 1)) k < n = O(n)
        # insert
        # BigO(O(n) + O(n) + O(k * log n)) k < n = O(n) + O(k log n) -> nLogn


import random
from typing import List


# 11 March 2025 Practice
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 12.02

        def euclideanDistance(p1):
            return ((p1[0] - 0) ** 2 + (p1[1] - 0) ** 2) ** (0.5)

        distances = []
        distancesToPoints = []

        for p in points:
            distance = euclideanDistance(p)
            distances.append(distance)
            distancesToPoints.append([distance, p])

        print(distancesToPoints)

        def quickSelect(points, k):
            if len(points) == 1:
                return points[0]
            pivot = random.choice(
                points
            )  # pivot = points[random.randint(0, len(points) - 1)]

            left = [x for x in points if x < pivot]
            mid = [x for x in points if x == pivot]
            right = [x for x in points if x > pivot]

            if k <= len(left):
                return quickSelect(left, k)
            elif k <= len(left) + len(mid):
                return mid[0]
            else:
                return quickSelect(right, k - (len(left) + len(mid)))

        targetDistance = quickSelect(distances, k)

        print(targetDistance)

        target = []

        for d, p in distancesToPoints:
            if targetDistance >= d:
                target.append(p)

        return target
        # 12.27 25 min


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if not points:
            return []

        listSD = []  # index length

        def lenToOrigin(x, y) -> float:
            return sqrt(x**2 + y**2)

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            # all sort by default is by index 0
            listSD.append([lenToOrigin(x, y), x, y])

        heapq.heapify(listSD)  # O(n)

        returnList = []

        for i in range(k):
            distance, x, y = heapq.heappop(listSD)
            returnList.append([x, y])

        return returnList

        # list1.sort(key = ) Check
        # BigO(O(n) + O(n) + O(k * 1)) k < n = O(n)
        # insert
        # BigO(O(n) + O(n) + O(k * log n)) k < n = O(n) + O(k log n) -> nLogn
