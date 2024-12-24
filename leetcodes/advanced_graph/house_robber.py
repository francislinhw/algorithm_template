# https://leetcode.com/problems/house-robber/
from typing import List
from collections import deque


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        stolen = 0
        q = deque(nums)

        while q:
            money = q.popleft()
            adjMoney = q.popleft()
            stolen = money + stolen

            nextMax = max(q)
            nextNextMax = q.popleft()

            while nextMax != nextNextMax:
                nextNextMax = q.popleft()

            q.appendleft(nextNextMax)
        
        return stolen

            
