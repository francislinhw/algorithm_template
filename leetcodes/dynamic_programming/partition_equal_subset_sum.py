#https://leetcode.com/problems/partition-equal-subset-sum/description/
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in reversed(range(len(nums))): # reversed or not, it doesn't matter
            newDp = dp.copy() # newDp = set() 
            for j in dp:
                newDp.add(j+nums[i])
                # newDp.add(j) # skip
            dp = newDp
        return True if target in dp else False
        
        

        

        