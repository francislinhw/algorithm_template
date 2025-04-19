# https://leetcode.com/problems/3sum-closest/description/


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 5.28
        # get min diff from the garget
        nums.sort()
        closest_sum = float("inf")

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  # 精準命中，直接回傳

        return closest_sum


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 5.28
        # get min diff from the garget
        res = [float("inf")]
        min_diff = [float("inf")]
        n = len(nums)

        def dfs(index, current_collection):
            if len(current_collection) == 3:
                current_sum = sum(current_collection)
                diff = abs(current_sum - target)
                if diff < min_diff[0]:
                    min_diff[0] = diff
                    res[0] = current_sum
                return

            if index >= n or len(current_collection) > 3:
                return

            # 包含當前數字
            dfs(index + 1, current_collection + [nums[index]])

            # 不包含當前數字
            dfs(index + 1, current_collection)

        dfs(0, [])
        return res[0]
