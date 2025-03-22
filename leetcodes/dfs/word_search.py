# https://leetcode.com/problems/word-search/description/
from typing import List


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 6.45 3.20 ->
        # Step 1: dfs compare
        # Step 2: for loop
        if word is None or board is None:
            return False

        rowLen = len(board)
        colLen = len(board[0])
        seen = set()

        def dfs(row, col, index):
            if index == len(word):
                return True

            if (
                row < 0
                or row >= rowLen
                or col < 0
                or col >= colLen
                or (row, col) in seen
                or board[row][col] != word[index]
            ):
                return False

            seen.add((row, col))

            result = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            seen.remove((row, col))

            return result

        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word is None or board is None:
            return False

        rowLen = len(board)
        colLen = len(board[0])
        seen = set()

        def dfs(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True

            if (
                row < 0
                or row >= rowLen
                or col < 0
                or col >= colLen
                or (row, col) in seen
                or board[row][col] != word[index]
            ):
                return False

            seen.add((row, col))

            result = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            seen.remove((row, col))

            return result

        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
