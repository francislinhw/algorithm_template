# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(x, current_subset):
            # Add the current subset to the result
            result.append(current_subset[:])  # Make a copy of current_subset

            # Explore further by including more elements in the subset
            for dx in range(x, len(nums)):
                current_subset.append(nums[dx])
                dfs(dx + 1, current_subset)  # Move to the next index
                current_subset.pop()  # Backtrack: remove the last added element

        # Start DFS from the first index with an empty subset
        dfs(0, [])

        return result


# 25 March 2025
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(x, current_subset):
            # Add the current subset to the result
            result.append(current_subset[:])  # Make a copy of current_subset

            # Explore further by including more elements in the subset
            for dx in range(x, len(nums)):
                current_subset.append(nums[dx])
                dfs(dx + 1, current_subset)  # Move to the next index
                current_subset.pop()  # Backtrack: remove the last added element

        # Start DFS from the first index with an empty subset
        dfs(0, [])

        return result


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []

        def dfs(i):
            if i >= len(nums):
                res.append(tmp.copy())
                return
