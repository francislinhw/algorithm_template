# https://leetcode.com/problems/gas-station/

from typing import List


# 13 March 2025 practice
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 11.03
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                if i + 1 < len(gas):
                    res = 1 + i
        return res


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        res = 0
        total = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]  # diff
            if total < 0:
                total = 0  # reset and see the next one
                if i + 1 < len(gas):
                    res = i + 1  # set to next one
        return res
