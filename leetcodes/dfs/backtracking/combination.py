from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                dfs(i, path + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1.26
        res = []

        def dfs(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, total + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 6.12
        result = []
        length = len(candidates)

        def backtrack(nums, index):
            if sum(nums) == target and nums not in result:
                result.append(nums[:])
                return
            if sum(nums) > target:
                return

            for i in range(index, length):
                nums.append(candidates[i])
                backtrack(nums, i)
                nums.pop()

        backtrack([], 0)

        return result  # 6.19 7 min


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
