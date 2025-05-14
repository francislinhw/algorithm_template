# https://leetcode.com/problems/search-in-rotated-sorted-array/

# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
# 11.52
# mapping = {}

# for i in range(len(nums)):
#     value = nums[i]
#     mapping[value] = i


# return mapping[target] if target in mapping else -1
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 判斷哪一邊是有序的
            if nums[left] <= nums[mid]:  # 左邊有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右邊有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
