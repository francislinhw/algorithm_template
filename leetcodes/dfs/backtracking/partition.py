from ast import List

# https://leetcode.com/problems/palindrome-partitioning/
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            return word == word[::-1]

        res = []

        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if isPalindrome(substring):
                    path.append(substring)
                    dfs(end, path)
                    path.pop()  # 回溯

        dfs(0, [])
        return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(chars: str) -> bool:
            l = 0
            r = len(chars) - 1

            isPar = True

            while l <= r:
                left = chars[l]
                right = chars[r]
                isPar = isPar and (left == right)
                l += 1
                r -= 1

            return isPar

        def backtrack(start: int, path: List[str]):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkP(s, l, r):
            while r >= l:
                if s[l] != s[r]:
                    return False
                r -= 1
                l += 1
            return True

        res = []
        tmp = []

        def backtrack(i):
            if i >= len(s):
                res.append(tmp.copy())
                return

            for j in range(i, len(s)):
                if checkP(s, i, j):
                    tmp.append(s[i : j + 1])
                    backtrack(j + 1)
                    tmp.pop()

        backtrack(0)
        return res
