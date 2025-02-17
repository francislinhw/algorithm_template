# https://leetcode.com/problems/number-of-1-bits/description/


class Solution:
    def hammingWeight(self, n: int) -> int:
        # 32 bits or 64 bits
        res = 0
        while n:
            res += n & 1
            n = n >> 1

        return res
