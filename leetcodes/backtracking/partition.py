from ast import List


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
