# https://leetcode.com/problems/permutations/description/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []
        seen = set()
        res = []
        curr = []

        def backtrack():
            if len(nums) == len(curr):
                res.append(curr.copy())  # curr[:] for python
                return

            for num in nums:
                if num not in seen:  # n!
                    seen.add(num)
                    curr.append(num)
                    backtrack()
                    seen.remove(num)
                    curr.pop()

        backtrack()
        return res
