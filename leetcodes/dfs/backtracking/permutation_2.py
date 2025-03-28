# https://leetcode.com/problems/permutations-ii/
from typing import List


from typing import List


# 27 March 2025
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        visited = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(
                nums
            ):  # If you like to skip the condition, you need to check existence before adding to result
                result.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                # Skip duplicates
                if (
                    i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]
                ):  # If you like to skip the condition, you need to check existence before adding to result
                    # 이전 숫자가 방문되지 않았다면 중복이므로 건너뜀
                    # This is to avoid generating duplicate permutations, because the same number can be used multiple times.
                    # For example, if we have [1, 2, 2], we don't want to generate [1, 2, 2] and [2, 1, 2] because they are the same.
                    # Why this condition means that the current number is a duplicate?
                    # Because if the current number is a duplicate, it means that the previous number is the same as the current number.
                    # So, if we have [1, 2, 2], we don't want to generate [1, 2, 2] and [2, 1, 2] because they are the same.
                    # You already have it at i -1
                    continue
                visited[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                visited[i] = False

        backtrack([])
        return result


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        tmp = []

        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
                continue
            cnt[num] += 1

        def dfs():
            if len(tmp) == len(nums):
                res.append(tmp.copy())
                return

            for n in cnt:
                if cnt[n] > 0:
                    tmp.append(n)
                    cnt[n] -= 1
                    dfs()
                    cnt[n] += 1
                    tmp.pop()

        dfs()
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []

        res = []
        currPerm = []

        numsMap = {}
        for number in nums:
            numsMap[number] = numsMap.get(number, 0) + 1

        def dfs(currPerm: List[int]):
            if len(currPerm) == len(nums):
                res.append(currPerm.copy())

            for number in numsMap:
                if numsMap[number] > 0:
                    currPerm.append(number)
                    numsMap[number] -= 1

                    dfs(currPerm)

                    currPerm.pop()
                    numsMap[number] += 1

        dfs(currPerm)
        return res


"""
		if not nums:
			return []
		
		result = set()

		def dfs(conbination: list):
			if len(conbnation) == len(nums):
				result.append(conbination)
			node = nums.pop()
			
			for num in nums:
				dfs(node + num)

			nums.append(node)
					


		dfs([])

		return result
"""
