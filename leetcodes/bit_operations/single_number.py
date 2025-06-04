# https://leetcode.com/problems/single-number/
# https://www.geeksforgeeks.org/python-bitwise-operators/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 12.03
        hashMap = {}

        result = set()

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
            if hashMap[num] == 1:
                result.add(num)
            else:
                result.remove(num)
        return list(result)[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i  # 0 ^ 1 = 1, 1 ^ 1 = 0, ^ is XOR
        return res
