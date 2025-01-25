# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if x == 0:
        #     return 0
        # if n == 0:
        #     return 1

        # def power(x, n):
        #     if n == 0:
        #         return 1
        #     if n == 1:
        #         return x
        #     return power(x, n/2) * power(x, n/2)

        # return power(x, n)

        if x == 0:
            return 0
        if n == 0:
            return 1

        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            res = helper(x, n // 2)
            res = res * res
            return res * x if n % 2 else res

        res = helper(x, abs(n))
        return res if n > 0 else 1 / res
