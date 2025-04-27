# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])  # max( .... )

        return max(dp)


# Example

# Input: nums = [10,9,2,5,3,7,101,18]
# dp = [1,1,4,3,3, 2,1,1] -> 4
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
