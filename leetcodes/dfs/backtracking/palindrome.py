# https://leetcode.com/problems/palindrome-partitioning/description/

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Example 1:

        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]
        Example 2:

        Input: s = "a"
        Output: [["a"]]
        """

        if not s:
            return []

        res = []
        tmp = []

        def dfs(i):
            if i >= len(s):
                res.append(tmp.copy())
                return

        dfs(0)
        return res
