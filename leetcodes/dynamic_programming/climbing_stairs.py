
class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        
        temp = [1] * 2

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