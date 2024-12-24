# https://leetcode.com/problems/unique-paths/
from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        currRow = [1] * n

        for r in reversed(range(m - 1)):
            for c in  reversed(range(n - 1)):
                currRow[c] = currRow[c] + currRow[c + 1]
        
        return currRow[0]
