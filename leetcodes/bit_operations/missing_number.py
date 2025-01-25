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
