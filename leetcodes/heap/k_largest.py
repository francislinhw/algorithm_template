# https://leetcode.com/problems/kth-largest-element-in-an-array/


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
