# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 9.47 3 March 2025 Practice
        if len(nums) == 1 and nums[0] == target:
            return 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            print("round 1", l)
            print(r)
            mid = (l + r) // 2
            val = nums[mid]

            # if nums[l] == target:
            #     return l
            # if nums[r] == target:
            #     return r

            if target > val:
                l = mid + 1
            elif target < val:
                r = mid - 1
            else:
                return mid

        return -1
        # 10.03 15 min

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # not O(n), must sorted, the fastest O(log(n))

        lPtr = 0
        rPtr = len(nums) - 1

        while rPtr >= lPtr:  # could be overlap
            midPtr = (rPtr + lPtr) // 2  # integer division
            if nums[midPtr] == target:
                return midPtr

            elif target > nums[midPtr]:
                lPtr = midPtr + 1
            else:
                rPtr = midPtr - 1

        return -1
