# https://leetcode.com/problems/house-robber/

from typing import List


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 11.47
        dp = [0 for _ in range(len(nums) + 2)]

        for i in reversed(range(len(nums))):
            rob = nums[i]
            dp[i] = max(rob + dp[i + 2], dp[i + 1])

        return dp[0]  # 12.00 13min


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # stolen = 0
        # stolenOne = 0

        # n = len(nums)

        # for i in (range(0, n, 2)):
        #     stolen = stolen + nums[i]

        # for i in (range(1, n, 2)):
        #     stolenOne = stolenOne + nums[i]

        # return max(stolen, stolenOne)

        nums.append(0)

        for i in reversed(range(len(nums) - 2)):
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])

        return nums[0]
