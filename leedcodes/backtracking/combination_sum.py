# https://leetcode.com/problems/combination-sum-ii/description/
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        res = []
        tmp = []

        candidates.sort()

        def dfs(i):
            if sum(tmp) == target:
                res.append(tmp.copy())
                return
            if i >= len(candidates) or sum(tmp) > target:
                return
            tmp.append(candidates[i])
            dfs(i + 1)
            tmp.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res
