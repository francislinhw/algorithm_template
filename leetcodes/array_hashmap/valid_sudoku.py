# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 8.13
        if not board:
            return False

        colDict = dict()
        rowDict = dict()
        blockDict = dict()

        legalList = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for i in range(len(board[0])):
            for j in range(len(board)):
                number = board[j][i]

                if number == ".":
                    continue
                if number not in legalList:
                    return False
                if i not in rowDict:
                    rowDict[i] = []
                if j not in colDict:
                    colDict[j] = []
                if (i // 3, j // 3) not in blockDict:
                    blockDict[(i // 3, j // 3)] = []
                if (
                    number in rowDict[i]
                    or number in colDict[j]
                    or number in blockDict[(i // 3, j // 3)]
                ):
                    return False

                rowDict[i].append(number)
                colDict[j].append(number)
                blockDict[(i // 3, j // 3)].append(number)

        return True  # 5 min


# 4 Apr 2025
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowDict = {}
        colDict = {}
        sqDict = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num == ".":
                    continue
                if j not in colDict:
                    colDict[j] = []
                if i not in rowDict:
                    rowDict[i] = []
                if (i // 3, j // 3) not in sqDict:
                    sqDict[(i // 3, j // 3)] = []  #
                if (
                    num in colDict[j]
                    or num in rowDict[i]
                    or num in sqDict[(i // 3, j // 3)]
                ):
                    return False
                colDict[j].append(num)
                rowDict[i].append(num)
                sqDict[(i // 3, j // 3)].append(num)
        return True


"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False

        isValid = True

        rows = board
        cols = [[".",".",".",".",".",".",".",".","." ] for i in range(9)]
        blocks = [[[] for i in range(3)] for j in range(3)]


        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                element = row[j]
                cols[j][i] = element
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                print(i)
                print(j)
                I = int(i/3)
                J = int(j/3)
                blocks[I][J].append(board[i][j])
                blocks[I][J].append(board[i][j+1])
                blocks[I][J].append(board[i][j+2])
                blocks[I][J].append(board[i+1][j])
                blocks[I][J].append(board[i+1][j+1])
                blocks[I][J].append(board[i+1][j+2])
                blocks[I][J].append(board[i+2][j])
                blocks[I][J].append(board[i+2][j+1])
                blocks[I][J].append(board[i+2][j+2])
        

        def checkNoDuplicate(row: list):
            numDict = {}
            for e in row:
                if e != ".":
                    if e not in numDict:
                        numDict[e] = 0
                    else:
                        return False
            return True
        
        for row in rows:
            res = checkNoDuplicate(row)
            if not res:
                return False

        print("block")
        print(blocks)

        for row in cols:
            res = checkNoDuplicate(row)
            if not res:
                return False      

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                I = int(i/3)
                J = int(j/3)
                row = blocks[I][J]
                res = checkNoDuplicate(row)
                if not res:
                    return False      

        return isValid # 30 min
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowDict = {}
        colDict = {}
        sqDict = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num == ".":
                    continue
                if j not in colDict:
                    colDict[j] = []
                if i not in rowDict:
                    rowDict[i] = []
                if (i // 3, j // 3) not in sqDict:
                    sqDict[(i // 3, j // 3)] = []  #
                if (
                    num in colDict[j]
                    or num in rowDict[i]
                    or num in sqDict[(i // 3, j // 3)]
                ):
                    return False
                colDict[j].append(num)
                rowDict[i].append(num)
                sqDict[(i // 3, j // 3)].append(num)
        return True

        #     rows = collections.defaultdict(list)
        # cols = collections.defaultdict(list)
        # pos = collections.defaultdict(list)

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == '.':
        #             continue

        #         if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in pos[(i//3, j//3)]):
        #             return False

        #         rows[i].append(board[i][j])
        #         cols[j].append(board[i][j])
        #         pos[(i//3,j//3)].append(board[i][j])
        # print(rows)
        # print(cols)
        # print(pos)

        # return True
