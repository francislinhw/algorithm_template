# https://leetcode.com/problems/partition-equal-subset-sum/description/
from typing import List


class Solution(object):
    def canPartition(self, nums):

        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = set([0])

        for num in nums:
            dp |= {x + num for x in dp}
            if target in dp:
                return True
        return False


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def dfs(index, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target or index >= len(nums):
                return False
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            # 選或不選當前數字
            pick = dfs(index + 1, curr_sum + nums[index])
            skip = dfs(index + 1, curr_sum)
            memo[(index, curr_sum)] = pick or skip
            return memo[(index, curr_sum)]

        return dfs(0, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in reversed(range(len(nums))):  # reversed or not, it doesn't matter
            newDp = dp.copy()  # newDp = set()
            for j in dp:
                newDp.add(j + nums[i])
                # newDp.add(j) # skip
            dp = newDp
        return True if target in dp else False
