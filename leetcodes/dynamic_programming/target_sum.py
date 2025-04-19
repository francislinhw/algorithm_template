# https://leetcode.com/problems/target-sum/

from typing import List


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 7.59
        memo = {}

        def dfs(index, total):
            key = (index, total)
            if key in memo:
                return memo[key]
            if index == len(nums):
                return 1 if total == target else 0
            count = dfs(index + 1, total + nums[index]) + dfs(
                index + 1, total - nums[index]
            )
            memo[key] = count
            return count

        return dfs(0, 0)


class Solution:
    # wrong version
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)

        seem = {}

        def dfs(prev: int, i: int):
            if i >= length:
                if prev not in seem:
                    seem[prev] = 0
                seem[prev] += 1
                return 0
            bigger = prev + nums[i]
            smaller = prev - nums[i]

            dfs(bigger, i + 1)
            dfs(smaller, i + 1)

        return seem[target]

    def findTargetSumWays_v2(self, nums: List[int], target: int) -> int:
        length = len(nums)

        dp = {}

        def dfs(prev: int, i: int):
            if i == length and prev == target:
                return 1
            if i >= length:
                return 0
            if (prev, i) in dp:
                return dp[(prev, i)]

            bigger = prev + nums[i]
            smaller = prev - nums[i]

            add = dfs(bigger, i + 1)
            sub = dfs(smaller, i + 1)
            dp[(prev, i)] = add + sub
            return dp[(prev, i)]

        return dfs(0, 0)

    # standard version
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, currSum):
            if i == len(nums) and currSum == target:
                return 1
            if i >= len(nums):
                return 0
            if (i, currSum) in dp:
                return dp[(i, currSum)]
            add = dfs(i + 1, currSum + nums[i])
            sub = dfs(i + 1, currSum - nums[i])
            dp[(i, currSum)] = add + sub
            return dp[(i, currSum)]

        return dfs(0, 0)
