from typing import List


class Solution(object):
    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in reversed(coins):
            tmpDp = [0] * (amount + 1)
            tmpDp[0] = 1
            for a in range(1, amount + 1):
                tmpDp[a] += dp[a]
                if a - c >= 0:
                    tmpDp[a] += tmpDp[a - c]
            dp = tmpDp
        return dp[-1]
