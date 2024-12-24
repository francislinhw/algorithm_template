# https://leetcode.com/problems/min-cost-climbing-stairs/description/
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
            
        n = len(cost) + 1
        cost.append(0)

        for i in reversed(range(n - 2)):
            cost[i] = cost[i] + min(cost[i +1], cost[i + 2])

        return min(cost[0], cost[1])