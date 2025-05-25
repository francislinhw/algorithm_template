# https://leetcode.com/problems/gas-station/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        currTank = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            currTank += diff

            if currTank < 0:
                start = i + 1
                currTank = 0

        return start


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
