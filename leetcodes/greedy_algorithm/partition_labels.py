# https://leetcode.com/problems/partition-labels/description/

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        charDict = {}
        for idx, val in enumerate(s):
            charDict[val] = idx

        res = []
        charCnt = 0
        lastIdx = 0

        for i in range(len(s)):
            charCnt += 1
            val = s[i]
            lastIdx = max(lastIdx, charDict[val])
            if i == lastIdx:
                res.append(charCnt)
                charCnt = 0

        return res
