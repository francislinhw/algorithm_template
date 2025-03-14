# https://leetcode.com/problems/kth-largest-element-in-an-array/

import random
from typing import List


# 11 March 2025 Practice
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 8.07
        def quickSelect(nums, k):
            if len(nums) == 1:
                return nums[0]

            pivot = random.choice(nums)

            left = [i for i in nums if i > pivot]
            middle = [i for i in nums if i == pivot]
            right = [i for i in nums if i < pivot]

            if len(left) >= k:
                return quickSelect(left, k)
            elif len(left) + len(middle) >= k:
                return middle[0]
            elif len(left) + len(middle) < k:
                return quickSelect(right, k - len(left) - len(middle))

        return quickSelect(nums, k)
        # 8.25


import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or not k:
            return None

        heapq.heapify(nums)

        target = (len(nums) - 1) - (k - 1)
        kLargest = None

        for i in range(len(nums)):
            kLargest = heapq.heappop(nums)
            if i == target:
                return kLargest
        return kLargest


# 215. Kth Largest Element in an Array

print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5)
