import heapq
from math import sqrt

# https://leetcode.com/problems/k-closest-points-to-origin/description/


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
