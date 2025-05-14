# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1.07
        # res = [-1, -1]
        # isFirst = True

        # for i in range(len(nums)):
        #     if nums[i] == target and isFirst:
        #         res[0] = i
        #         isFirst = False
        #     if nums[i] == target and not isFirst:
        #         res[1] = i

        l = 0
        r = len(nums) - 1
        goal = float("inf")

        while l <= r:
            m = (l + r) // 2
            mid = nums[m]

            if mid == target:
                goal = m
                break
            elif mid > target:
                r = m - 1
            elif mid < target:
                l = m + 1

        if goal == float("inf"):
            return [-1, -1]

        res = [goal, goal]

        i = 0
        while True:
            if goal - i < 0:
                break
            if nums[goal - i] == target:
                res[0] = goal - i
            else:
                break
            i += 1
        j = 0
        while True:
            if goal + j > len(nums) - 1:
                break
            if nums[goal + j] == target:
                res[1] = goal + j
            else:
                break
            j += 1

        return res  # 14 min
