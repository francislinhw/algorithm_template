# https://leetcode.com/problems/jump-game-ii/


class Solution(object):
    def jump(self, nums):
        # 8.46
        dp = [float("inf") for i in range(len(nums) - 1)] + [0, 0]

        for i in reversed(range(len(nums) - 1)):
            currentStep = nums[i]
            s = dp[i + 1 : min(i + currentStep + 1, len(dp))]
            if s != []:
                dp[i] = 1 + min(s)

        return dp[0]  # 40
