# https://leetcode.com/problems/gray-code/
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 10.59
        res = [0]
        for i in range(n):
            add = 1 << i  # 相當於 2^i
            print(i, add)
            for j in reversed(res):
                res.append(j + add)
                print(res)
        return res
