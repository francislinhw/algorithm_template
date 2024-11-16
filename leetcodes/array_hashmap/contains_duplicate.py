# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenMap = set()

        for number in nums:
            if number in seenMap:
                return True
            seenMap.add(number)

        return False
