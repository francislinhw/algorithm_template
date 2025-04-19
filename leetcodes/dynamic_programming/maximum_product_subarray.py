# https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class Solution(object):
    def maxProduct(self, nums):
        # 10.57

        if not nums:
            return 0

        maxProduct = nums[0]
        currMax, currMin = nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                currMax, currMin = currMin, currMax  # 交換

            currMax = max(num, currMax * num)
            currMin = min(num, currMin * num)

            maxProduct = max(maxProduct, currMax)

        return maxProduct


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        currMax = 1
        currMin = 1

        for num in nums:
            if num == 0:
                currMax = 1
                currMin = 1
                continue

            tmp = currMax
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(num * tmp, num * currMin, num)
            res = max(currMax, currMin, res)
        return res
