# https://leetcode.com/problems/4sum/


class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res


class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()  # 有助於剪枝
        visited = set()
        result = []

        def dfs(collection, index):
            if len(collection) == 4:
                if sum(collection) == target:
                    key = tuple(collection)
                    if key not in visited:
                        visited.add(key)
                        result.append(list(collection))
                return
            if index >= len(nums):
                return

            # 剪枝：若加了也不會超過 4 個，就嘗試加入
            collection.append(nums[index])
            dfs(collection, index + 1)
            collection.pop()  # 回溯

            # 不選擇這個數字
            dfs(collection, index + 1)

        dfs([], 0)
        return result
