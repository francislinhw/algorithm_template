# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # res = []

        # number = 0

        # for i in reversed(range(len(digits))):
        #     number += digits[i] * 10**((len(digits)-1) - i)

        # number += 1

        # for digit in str(number):
        #     res.append(int(digit))

        # return res

        res = []
        currNum = ""
        for num in digits:
            currNum += str(num)

        tmp = int(currNum) + 1
        for num in str(tmp):
            res.append(int(num))

        return res
