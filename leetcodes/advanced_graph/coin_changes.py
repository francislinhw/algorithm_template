# https://leetcode.com/problems/coin-change/description/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for amt in range(len(dp)):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1+dp[amt-coin])
        return dp[amount] if dp[amount] != float('inf') else -1