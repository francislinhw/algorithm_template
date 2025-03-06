from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 11.41

        for i in range(len(nums)):
            if target <= nums[i]:
                return i

        return len(nums)
        # 1145 4 min

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

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
