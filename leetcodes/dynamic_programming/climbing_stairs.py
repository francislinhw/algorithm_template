# https://leetcode.com/problems/climbing-stairs/submissions/1609238096/


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 10.06
        dp = [0 for _ in range(n - 1)] + [1, 1]

        for _ in reversed(range(n - 1)):
            dp[_] = dp[_ + 1] + dp[_ + 2]

        return dp[0]  # 6 min


class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0

        temp = [1] * 2  # set the first two elements to 1 to satisfy the base case
        # base case: n = 1, return 1
        # base case: n = 2, return 2

        for i in reversed(range(n - 1)):
            tem = temp[0] + temp[1]
            temp[1] = temp[0]
            temp[0] = tem

        return temp[0]


"""
#       one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
"""
