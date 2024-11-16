from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates:
            return []
        res = []
        tmp = []

        def dfs(i):
            if sum(tmp) == target:
                res.append(tmp.copy())
                return
            if i >= len(candidates) or sum(tmp) > target:
                return
            tmp.append(candidates[i])
            dfs(i)
            tmp.pop()
            dfs(i + 1)

        dfs(0)
        return res
        # space complexity: O(n)
        # time complexity: O(2^n)
