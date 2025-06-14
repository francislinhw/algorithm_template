# https://leetcode.com/problems/subsets-ii/

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 8.57

        nums.sort()
        result = []
        path = []

        def backtrack(start: int):
            result.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result


# 25 March 2025 Practice
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 10.39

        result = set()
        nums.sort()

        def dfs(x, subset):
            if tuple(subset) not in result:
                result.add(tuple(subset[:]))

            for dx in range(x, len(nums)):
                subset.append(nums[dx])
                dfs(dx + 1, subset)
                subset.pop()

        dfs(0, [])

        result = list(result)

        return result


# https://leetcode.com/problems/subsets-ii/description/

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        tmp = []

        def backtrack(i):
            if i == len(nums):
                res.append(tmp.copy())
                return

            tmp.append(nums[i])
            backtrack(i + 1)
            tmp.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res
