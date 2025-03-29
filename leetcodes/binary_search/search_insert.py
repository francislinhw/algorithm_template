# https://leetcode.com/problems/search-insert-position/


# 29 March 2025 Practice
class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 6.46
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # When target is not found, left is the insertion position.
        return left


class Solution:
    def searchInsert(self, nums, target):
        # not O(n), must sorted, the fastest O(log(n))

        lPtr = 0
        rPtr = len(nums) - 1

        while rPtr >= lPtr:
            midPtr = (rPtr + lPtr) // 2
            if nums[midPtr] == target:
                countIndex = midPtr
                returnPtr = midPtr
                while countIndex >= 0:
                    if nums[countIndex] == target:
                        returnPtr = countIndex
                        countIndex -= 1
                    else:
                        break
                return returnPtr

            elif target > nums[midPtr]:
                lPtr = midPtr + 1
            else:
                rPtr = midPtr - 1

        return lPtr
