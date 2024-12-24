# https://leetcode.com/problems/house-robber-ii/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            nums.append(0)
            for i in reversed(range(len(nums)-2)):
                nums[i] = max(nums[i] + nums[i+2], nums[i+1])
            
            return nums[0]

        rob1 = helper(nums[1:])
        rob2 = helper(nums[:-1])            

        return max(rob1, rob2)