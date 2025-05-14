# https://leetcode.com/problems/powx-n/


class Solution(object):
    def myPow(self, x, n):
        # 11.47

        if x == 0:
            return 0
        if n == 0:
            return 1

        def powerf(number, power):
            if power == 0:
                return 1
            half = powerf(number, power // 2)
            if power % 2 == 0:
                return half * half
            else:
                return half * half * number

        result = powerf(x, abs(n))
        return result if n > 0 else 1 / result


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
