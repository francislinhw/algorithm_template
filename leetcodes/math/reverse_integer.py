# https://leetcode.com/problems/reverse-integer/description/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0

        sign = -1 if x < 0 else 1

        total = 0

        stringNumber = str(abs(x))

        for i in range(len(stringNumber)):
            total += int(stringNumber[i]) * (10 ** (i))

        if total * sign > (2**31 - 1) or total * sign < (-(2**31)):
            return 0

        return total * sign
