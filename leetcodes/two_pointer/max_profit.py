# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 9.04
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 9.04
        l = 0  # 買進日
        r = 1  # 賣出日
        max_profit = 0

        while r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])
            if prices[r] <= prices[l]:
                l = r
                r = l
            r += 1

        return max_profit


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
