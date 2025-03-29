# https://leetcode.com/problems/combination-sum-ii/description/


# 29 March 2025 Practice
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # sort to handle duplicates
        result = []

        def backtrack(start, current_sum, current_list):
            # Check if we've reached the target sum
            if current_sum == target:
                result.append(current_list[:])
                return
            # If we exceed the target, there's no point in continuing
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates: only use the first candidate among duplicates at this level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose the candidate
                current_list.append(candidates[i])
                # Recurse: move to the next index as each candidate can only be used once
                backtrack(i + 1, current_sum + candidates[i], current_list)
                # Backtrack: remove the candidate from the current combination
                current_list.pop()

        backtrack(0, 0, [])
        return result


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
