# https://leetcode.com/problems/surrounded-regions/

from typing import List


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 11.29
        # Step 1: For Loop

        # Step 2: DFS to find all the O
        visited = set()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(node):
            element = board[node[1]][node[0]]
            visited.add(tuple(node))

            if (
                element == "X"
                or node[1] == 0
                or node[0] == 0
                or node[1] == len(board) - 1
                or node[0] == len(board) - 1
            ):
                return
            elif element == "O":
                up = board[node[1] + 1][node[0]]
                down = board[node[1] - 1][node[0]]
                left = board[node[1]][node[0] - 1]
                right = board[node[1]][node[0] + 1]
                if up == "X" and down == "X" and left == "X" and right == "X":
                    board[node[1]][node[0]] = "X"
                    dfs(node + direction[0])
                    dfs(node + direction[1])
                    dfs(node + direction[2])
                    dfs(node + direction[3])

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs([i, j])


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])
        visited = set()  # Save the points of "O" starting from the boundary

        def dfs(row: int, col: int) -> None:
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != "O"
                or (row, col) in visited
            ):
                return

            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)

        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"
