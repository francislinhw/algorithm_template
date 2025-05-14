# https://leetcode.com/problems/sort-colors/
from typing import List


# Dutch National Flag Problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 11.02

        def merge(left, right):
            res = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                l = left[i]
                r = right[j]
                if l < r:
                    res.append(l)
                    i += 1
                else:
                    res.append(r)
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res

        def divide(nums):
            if len(nums) <= 1:
                return nums
            m = len(nums) // 2
            left = divide(nums[:m])
            right = divide(nums[m:])
            return merge(left, right)

        sorted_nums = divide(nums)
        for i in range(len(nums)):
            nums[i] = sorted_nums[i]
