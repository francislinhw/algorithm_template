# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 4.01
        hashMap = {}

        for i in nums:
            if i not in hashMap:
                hashMap[i] = 0
            hashMap[i] += 1

            if hashMap[i] > 1:
                return True

        return False
        # 4.03

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # set_nums = set(nums) # O(n) is from this.
        #
        # if len(set_nums) != len(nums):
        #    return True
        # else:
        #    return False

        # Standard solution
        set_nums = set()

        for n in nums:
            if n in set_nums:
                return True

            set_nums.add(n)

        return False
