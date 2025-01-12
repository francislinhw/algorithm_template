from ast import List


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
