# https://leetcode.com/problems/maximum-subarray/

from typing import List


# 13 March 2025
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        l = 0
        r = 0

        currentSum = 0
        res = 0

        while r < len(nums):
            subNums = nums[l:r]
            currentSum = sum(subNums)
            if sum(subNums) >= 0:
                r += 1
                res = max(res, currentSum)
            else:
                l = r
                r += 1

        return res

        # if not nums:
        #     return None

        # l = 0
        # r = 0

        # currentSum = 0
        # res = 0

        # while r < len(nums):
        #     subNums = nums[l:r]
        #     currentSum = (sum(subNums))
        #     if currentSum >= 0:
        #         r += 1
        #         res = max(res, currentSum)
        #     else:
        #         l = r
        #         r += 1

        # return res
