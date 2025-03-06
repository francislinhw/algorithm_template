# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List


# 4 March Practice
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 9.35
        if len(arr) == 1:
            return [-1]

        result = [-1 for i in range(len(arr))]

        maxVal = arr[-1]

        indicator = len(arr) - 2

        for i in reversed(arr):
            if indicator < 0:
                break
            maxVal = max(maxVal, i)
            result[indicator] = maxVal
            indicator -= 1

        return result  # 9.44 8 min


class Solution(object):

    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        greatestNum = float("-inf")

        # range(len(arr), -1, -1)

        for i in reversed(range(len(arr))):
            currNum = arr[i]
            arr[i] = greatestNum
            if currNum > greatestNum:
                greatestNum = currNum

        arr[-1] = -1
        return arr
