# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 1.28
        if target > nums[-1]:
            # left part
            prev = nums[-1]
            for i in range(len(nums)):
                curr = nums[i]
                if curr < prev:
                    return False
                if curr == target:
                    return True
                prev = curr
        elif target < nums[-1]:
            # right part
            prev = nums[-1]
            for i in reversed(range(len(nums))):
                curr = nums[i]
                if curr > prev:
                    return False
                if curr == target:
                    return True
                prev = curr
        else:
            return True

        return False

        # return True if target in nums else False


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # 去除重複值造成的困擾
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:  # 左側是有序的
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右側是有序的
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
