# https://leetcode.com/problems/single-number/
# https://www.geeksforgeeks.org/python-bitwise-operators/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
