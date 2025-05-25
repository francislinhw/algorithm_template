# https://leetcode.com/problems/partition-labels/description/

from typing import List

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Record the last occurrence of each character
        last_occurrence = {char: i for i, char in enumerate(s)}

        res = []
        start = 0
        end = 0

        # Step 2: Walk through the string and find partitions
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 9.20

        positionMap = {}
        # First Step: Create the position Map char: last position
        for i in range(len(s)):
            char = s[i]
            positionMap[char] = i

        print(positionMap)

        # Second Step: for loop the string and check if words within the string are having the last position within if not update, if yes save it
        last = []

        lastPosition = -float("inf")

        for i in range(len(s)):
            char = s[i]
            lastPosition = max(positionMap[char], lastPosition)
            if lastPosition == i:
                last.append(1 + i)

        res = []
        res.append(last[0])

        for i in range(1, len(last)):
            res.append(last[i] - last[i - 1])

        return res  # 18 min


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
