from typing import List


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
