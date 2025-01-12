# https://leetcode.com/problems/n-queens-ii/
class Solution:
    def totalNQueens(self, n: int) -> int:
        if not n:
            return []

        result = []

        board = [["."] * n for i in range(n)]
        # diagonal from upperright to the down left = n
        # reversly, abs(diff) = n
        positiveDiagnalSeen = set()
        negativeDiagnalSeen = set()
        columnSeen = set()

        startFromRow = 0

        def placement(row: int, board: list):
            if row == n:  # or col > n - 1:
                result.append(["".join(listBoard) for listBoard in board.copy()])
                return

            for col in range(n):
                markPositive = row + col
                markNegative = row - col

                if (
                    board[row][col] != "Q"
                    and markNegative not in negativeDiagnalSeen
                    and markPositive not in positiveDiagnalSeen
                    and col not in columnSeen
                ):
                    board[row][col] = "Q"
                    negativeDiagnalSeen.add(markNegative)
                    positiveDiagnalSeen.add(markPositive)
                    columnSeen.add(col)

                    placement(row + 1, board)

                    board[row][col] = "."
                    negativeDiagnalSeen.discard(markNegative)
                    positiveDiagnalSeen.discard(markPositive)
                    columnSeen.discard(col)

        placement(startFromRow, board)

        return len(result)
