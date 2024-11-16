# https://leetcode.com/problems/max-area-of-island/
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        maxArea = 0
