# https://leetcode.com/problems/combinations/

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 7.32
        result = []

        def backtrack(word, index):
            if len(word) == k:  # and word not in result:
                result.append(word[:])
                return
            if len(word) >= k:
                return
            for i in range(index, n + 1):
                # if i in word:
                #     continue
                word.append(i)
                backtrack(word, i + 1)
                word.pop()

        backtrack([], 1)

        return result


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n or not k:
            return []

        def dfs(start: int) -> None:
            if len(tmp) == k:
                res.append(tmp.copy())
                return

            for i in range(start, n + 1):
                tmp.append(i)
                dfs(i + 1)
                tmp.pop()

        res = []
        tmp = []

        dfs(1)
        return res


"""
        nList = [n for n in range(1,n+1)]
        res = []
        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i >= len(nList):
                return
            
            curr.append(nList[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        dfs(0, [])
        return res
        """


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        if not n or not k:
            return []

        def dfs(start: int) -> None:
            if len(tmp) == k:
                res.append(tmp.copy())
                return

            for i in range(start, n + 1):
                tmp.append(i)
                dfs(i + 1)
                tmp.pop()

        res = []
        tmp = []

        dfs(1)
        return res


"""
        nList = [n for n in range(1,n+1)]
        res = []
        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i >= len(nList):
                return
            
            curr.append(nList[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        dfs(0, [])
        return res
        """

# 77. Combinations
n = 4
k = 2

solution = Solution().combine(n, k)

print(solution == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
