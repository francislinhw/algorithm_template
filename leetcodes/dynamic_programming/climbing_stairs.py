# https://leetcode.com/problems/climbing-stairs/submissions/1609238096/
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
