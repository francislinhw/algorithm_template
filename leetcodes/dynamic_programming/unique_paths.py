# https://leetcode.com/problems/unique-paths/
from typing import List


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 7.44
        block = [1 for _ in range(n)]

        for j in range(m - 1):
            for i in reversed(range(n - 1)):
                block[i] = block[i + 1] + block[i]

        return block[0]  # 8 min


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        currRow = [1] * n

        for r in reversed(range(m - 1)):
            for c in reversed(range(n - 1)):
                currRow[c] = currRow[c] + currRow[c + 1]

        return currRow[0]
