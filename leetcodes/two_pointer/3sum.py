# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        l = 0
        r = 0
        pivot = 0

        result = []

        nums.sort()

        for i in range(len(nums)):
            pivot = i
            l = pivot - 1
            r = pivot + 1

            while pivot >= 1 and pivot < len(nums) and l >= 0 and r < len(nums):
                left = nums[l]
                middle = nums[pivot]
                right = nums[r]
                summantion = left + middle + right

                if summantion == 0:
                    temp = [left, middle, right]
                    if temp not in result:
                        result.append(temp)
                    l -= 1
                    r += 1

                elif summantion < 0:
                    r += 1

                elif summantion > 0:
                    l -= 1

                # if l <= 0 and r < len(nums):
                #     l += 1
                # if l < 0 and r >= len(nums):
                #     r -= 1

        return result  # 10 mins

        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return res
