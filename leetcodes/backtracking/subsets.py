# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []

        def dfs(i):
            if i >= len(nums):
                res.append(tmp.copy())
                return
