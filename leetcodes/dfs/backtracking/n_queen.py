from ast import List


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []

        def backtrack(row, cols, diag1, diag2, path):
            if row == n:
                board = []
                for i in path:
                    row_str = ["."] * n
                    row_str[i] = "Q"
                    board.append("".join(row_str))
                res.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                path.append(col)

                backtrack(row + 1, cols, diag1, diag2, path)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                path.pop()

        backtrack(0, set(), set(), set(), [])
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        posSlope = set()  # (r+c)
        negSlope = set()  # (r-c)
        res = []
        tmp = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                holder = tmp.copy()
                tmpHolder = ["".join(h) for h in holder]
                res.append(tmpHolder)

            for c in range(n):
                if c in col or (r + c) in posSlope or (r - c) in negSlope:
                    continue

                col.add(c)
                posSlope.add(r + c)
                negSlope.add(r - c)
                tmp[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posSlope.remove(r + c)
                negSlope.remove(r - c)
                tmp[r][c] = "."

        backtrack(0)
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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
                print("ROW", row)
                print(board)
                result.append(["".join(listBoard) for listBoard in board.copy()])
                return

            for col in range(n):
                markPositive = row + col
                print("possitive", markPositive)
                print("p Seen", positiveDiagnalSeen)
                markNegative = row - col
                print("negative", markNegative)
                print("n Seen", negativeDiagnalSeen)

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
                    print(board)

                    placement(row + 1, board)

                    board[row][col] = "."
                    negativeDiagnalSeen.discard(markNegative)
                    positiveDiagnalSeen.discard(markPositive)
                    columnSeen.discard(col)

        placement(startFromRow, board)

        return result
