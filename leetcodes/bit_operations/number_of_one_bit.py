# https://leetcode.com/problems/number-of-1-bits/description/


# 16 March 2025
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 32 bits or 64 bits
        # res = 0
        # while n:
        #     res += n & 1
        #     n = n >> 1

        # return res
        """
        :type n: int
        :rtype: int
        """
        binary_str = bin(n)[2:]  # 轉換為二進位字串，去掉 "0b" 前綴

        return binary_str.count("1")  # 直接計算 '1' 的數量


class Solution:
    def hammingWeight(self, n: int) -> int:
        # 32 bits or 64 bits
        res = 0
        while n:
            res += n & 1  # & is AND
            n = n >> 1  # shift right

        return res
