# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        currMax = 1
        currMin = 1
        
        for num in nums:
            if num == 0:
                currMax = 1
                currMin = 1
                continue
            
            tmp = currMax
            currMax = max(num*currMax, num*currMin, num)
            currMin = min(num*tmp, num*currMin, num)
            res = max(currMax, currMin, res)
        return res