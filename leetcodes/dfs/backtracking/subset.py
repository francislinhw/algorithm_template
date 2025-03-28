from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(start, subset):
            # If the sum of the current subset equals the target, add it to the result
            if sum(subset) == target:
                result.append(subset[:])  # Make a copy of the current subset
                return
            # If the sum exceeds the target, stop further exploration
            if sum(subset) > target:
                return

            for i in range(start, len(candidates)):
                # Add the current candidate to the subset
                subset.append(candidates[i])
                # Recursively try the next candidates (allow repetition)
                dfs(i, subset)
                # Backtrack: remove the last added element
                subset.pop()

        # Start DFS from the first index with an empty subset
        dfs(0, [])

        return result


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
