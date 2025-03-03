# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """

        leftPtr = 0
        rightPtr = 0
        profit = 0

        while rightPtr < len(prices):
            if prices[leftPtr] > prices[rightPtr]:
                leftPtr = rightPtr  # template

            profit = max(prices[rightPtr] - prices[leftPtr], profit)
            rightPtr += 1  # template

        return profit
