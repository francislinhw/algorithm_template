# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        res = 0

        for i in range(n):
            res = res ^ nums[i]

        for j in range(n + 1):
            res = res ^ j

        return res


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 12.33
        length = len(nums)

        for i in range(len(nums) + 1):
            if length not in nums:
                return length
            length = length - 1


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        res = 0

        for i in range(n):
            res = res ^ nums[i]

        for j in range(n + 1):
            res = res ^ j

        return res
