# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 9.12

        newNums = [[nums[i], i] for i in range(len(nums))]

        newNums.sort()

        l = 0
        r = len(nums) - 1

        while r > l:
            num1 = newNums[l][0]
            num2 = newNums[r][0]

            total = num1 + num2

            if total == target:
                if newNums[l][1] > newNums[r][1]:
                    return [newNums[r][1], newNums[l][1]]
                else:
                    return [newNums[l][1], newNums[r][1]]

            elif total > target:
                r -= 1
            elif total < target:
                l += 1

    # 9.28 16 min

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # numsPositionHash = {}
        # for i in range(len(nums)):
        #     numsPositionHash[nums[i]] = i
        #
        # nums.sort()
        #
        # lPtr = 0
        # rPtr = len(nums) - 1
        #
        # while lPtr < rPtr:
        #     if nums[lPtr] + nums[rPtr] > target:
        #         rPtr -= 1
        #     elif  nums[lPtr] + nums[rPtr] < target:
        #         lPtr += 1
        #     else:
        #         if numsPositionHash[nums[lPtr]] == numsPositionHash[nums[rPtr]]:
        #             return [numsPositionHash[nums[lPtr]]-1, numsPositionHash[nums[rPtr]]]
        #         return [numsPositionHash[nums[lPtr]], numsPositionHash[nums[rPtr]]]

        newToOldIndexMap = {}

        for i in range(len(nums)):
            newToOldIndexMap[i] = i

        while True:
            hasExchange = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    temp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = temp
                    newToOldIndexMap[i] = i + 1
                    newToOldIndexMap[i + 1] = i
                    hasExchange = True

            if hasExchange == False:
                break

            hasExchange = False

        lPtr = 0
        rPtr = len(nums) - 1

        while lPtr < rPtr:
            if nums[lPtr] + nums[rPtr] > target:
                rPtr -= 1
            elif nums[lPtr] + nums[rPtr] < target:
                lPtr += 1
            else:
                return [newToOldIndexMap[lPtr], newToOldIndexMap[rPtr]]
