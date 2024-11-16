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
