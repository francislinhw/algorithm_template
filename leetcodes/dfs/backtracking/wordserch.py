# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])

        def dfs(x, y, string, visited):
            if x < 0 or y < 0 or x >= cols or y >= rows:
                return False
            if (x, y) in visited:
                return False

            string += board[y][x]

            if not word.startswith(string):
                return False
            if string == word:
                return True

            visited.add((x, y))
            for dx, dy in directions:
                if dfs(x + dx, y + dy, string, visited):
                    return True
            visited.remove((x, y))
            return False

        for y in range(rows):
            for x in range(cols):
                if dfs(x, y, "", set()):
                    return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])

        def dfs(x, y, idx, visited):
            if x < 0 or y < 0 or x >= cols or y >= rows:
                return False
            if (x, y) in visited:
                return False
            if board[y][x] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True

            visited.add((x, y))
            for dx, dy in directions:
                if dfs(x + dx, y + dy, idx + 1, visited):
                    return True
            visited.remove((x, y))
            return False

        for y in range(rows):
            for x in range(cols):
                if dfs(x, y, 0, set()):
                    return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        xLen = len(board[0])
        yLen = len(board)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, index):
            # If we've matched the entire word
            if index == len(word):
                return True
            # If out of bounds or current cell does not match the required character
            if x < 0 or y < 0 or x >= xLen or y >= yLen or board[y][x] != word[index]:
                return False

            # Temporarily mark the current cell as visited
            temp = board[y][x]
            board[y][x] = "/"

            # Explore all possible directions
            for dx, dy in directions:
                if dfs(x + dx, y + dy, index + 1):
                    return True

            # Backtrack: restore the current cell
            board[y][x] = temp
            return False

        # Start DFS from every cell that matches the first letter of the word
        for i in range(xLen):
            for j in range(yLen):
                if board[j][i] == word[0]:  # Match the first letter of the word
                    if dfs(i, j, 0):
                        return True

        return False


# 24 March practice
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        xLen = len(board[0])
        yLen = len(board)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, index):
            # If we've matched the entire word
            if index == len(word):
                return True
            # If out of bounds or current cell does not match the required character
            if x < 0 or y < 0 or x >= xLen or y >= yLen or board[y][x] != word[index]:
                return False

            # Temporarily mark the current cell as visited
            temp = board[y][x]
            board[y][x] = "/"

            # Explore all possible directions
            for dx, dy in directions:
                if dfs(x + dx, y + dy, index + 1):
                    return True

            # Backtrack: restore the current cell
            board[y][x] = temp
            return False

        # Start DFS from every cell that matches the first letter of the word
        for i in range(xLen):
            for j in range(yLen):
                if board[j][i] == word[0]:  # Match the first letter of the word
                    if dfs(i, j, 0):
                        return True

        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #         #The time complexity would be O(n*m*4^n)

        row = len(board)
        col = len(board[0])
        seen = set()

        def dfs(r, c, i, currWord):
            if currWord == word:
                return True

            if (
                r < 0
                or c < 0
                or r >= row
                or c >= col
                or word[i] != board[r][c]
                or (r, c) in seen
            ):
                return False

            seen.add((r, c))
            top = dfs(r - 1, c, i + 1, currWord + board[r][c])
            down = dfs(r + 1, c, i + 1, currWord + board[r][c])
            left = dfs(r, c - 1, i + 1, currWord + board[r][c])
            right = dfs(r, c + 1, i + 1, currWord + board[r][c])
            seen.remove((r, c))  # backtracking sprit
            return top or down or left or right

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0, ""):
                    return True
        return False
