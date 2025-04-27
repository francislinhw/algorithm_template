# https://leetcode.com/problems/coin-change/description/
from typing import List


class Solution(object):
    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] + [float("inf")] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


class Solution(object):
    def coinChange(self, coins, amount):
        # 12.10
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0  # base case: amount 0 needs 0 coins

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for amt in range(len(dp)):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        return dp[amount] if dp[amount] != float("inf") else -1
