# https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 7.04
        if len(nums) == 1:
            return nums[0]

        def houseRobber(flatten):
            dp = [0 for _ in range(len(flatten) + 2)]

            for i in reversed(range(len(flatten))):
                dp[i] = max(flatten[i] + dp[i + 2], dp[i + 1])

            return dp[0]

        withouthead = [nums[i] for i in range(1, len(nums))]
        withhead = [nums[i] for i in range(0, len(nums) - 1)]

        return max(houseRobber(withouthead), houseRobber(withhead))


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            nums.append(0)
            for i in reversed(range(len(nums) - 2)):
                nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])

            return nums[0]

        rob1 = helper(nums[1:])
        rob2 = helper(nums[:-1])

        return max(rob1, rob2)
