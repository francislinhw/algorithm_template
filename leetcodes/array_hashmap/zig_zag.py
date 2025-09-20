# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curRow, step = 0, 1

        for ch in s:
            rows[curRow] += ch
            # 方向轉折
            if curRow == 0:
                step = 1
            elif curRow == numRows - 1:
                step = -1
            curRow += step

        return "".join(rows)


# 15 April 2025
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        cycle_len = 2 * numRows - 2
        hashMap = {i: [] for i in range(numRows)}

        for j in range(len(s)):
            index = j % cycle_len
            if index >= numRows:
                index = cycle_len - index  # 折返走

            hashMap[index].append(s[j])

        res = ""
        for i in range(numRows):
            res += "".join(hashMap[i])
        return res
