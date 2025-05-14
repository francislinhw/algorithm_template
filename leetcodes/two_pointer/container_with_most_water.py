# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 6.57
        if not height:
            return 0

        l = 0
        r = len(height) - 1

        maxArea = 0

        while l < r:
            left = height[l]
            right = height[r]
            maxArea = max(maxArea, (r - l) * min(left, right))
            if left < right:
                l += 1
            else:
                r -= 1

        return maxArea  # 5 min


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # VERSION ONE
        # if not height:
        #     return 0

        # l = 0
        # r = 0
        # areaMax = 0
        # currentArea = 0

        # while r < len(height) and l < len(height) :
        #     currentArea = (r - l) * min(height[r], height[l])
        #     areaMax = max(currentArea, areaMax)

        #     if r == len(height) - 1:
        #         l += 1
        #         r = l
        #     else:
        #         r += 1

        # return areaMax

        # VERSION TWO: After hint, it is eazy
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        areaMax = 0
        currentArea = 0

        while r < len(height) and l < len(height) and r >= 0 and l >= 0:
            currentArea = (r - l) * min(height[r], height[l])
            areaMax = max(currentArea, areaMax)

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return areaMax


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         if len(height) <= 0:
#             return 0

#         l = 0
#         r = len(height) - 1
#         maxArea = 0

#         while r > l:
#             leftH = height[l]
#             rightH = height[r]
#             currentArea = min(leftH, rightH) * (r - l)
#             maxArea = max(maxArea, currentArea)

#             if leftH < rightH:
#                 l += 1
#             else:
#                 r -= 1
#         return maxArea
