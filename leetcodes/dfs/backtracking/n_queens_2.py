# https://leetcode.com/problems/n-queens-ii/


class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 5.46
        # put anywhere and check if that is workable
        # any place that I can decide to be

        # Symbol: "O" Empty, "X" -> Queen
        self.count = 0

        def backtrack(row, cols, diags1, diags2):
            if row == n:
                self.count += 1
                return

            for col in range(n):
                if col in cols or (row - col) in diags1 or (row + col) in diags2:
                    continue
                # Choose
                cols.add(col)
                diags1.add(row - col)
                diags2.add(row + col)
                # Explore
                backtrack(row + 1, cols, diags1, diags2)
                # Un-choose
                cols.remove(col)
                diags1.remove(row - col)
                diags2.remove(row + col)

        backtrack(0, set(), set(), set())
        return self.count


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
                markPositive = (
                    row + col
                )  # It can be mark as diagnal because the sum of row and col is the same for all diagnals
                markNegative = (
                    row - col
                )  # It can be mark as diagnal because the diff of row and col is the same for all diagnals

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
