# https://leetcode.com/problems/subsets-ii/

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        nums.sort()

        def dfs(i):
