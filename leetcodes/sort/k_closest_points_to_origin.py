# https://leetcode.com/problems/k-closest-points-to-origin/description/?envType=problem-list-v2&envId=quickselect
# 2 March 2025 practice
from typing import List
import random


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
            pivot = random.choice(points)

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
