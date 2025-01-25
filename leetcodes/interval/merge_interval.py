# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intuition: stack
        # 100% sort in advanced

        intervals.sort()  # see lambda sort n log n + log n

        stack = []
        stack.append(intervals[0])

        for start, end in intervals[1:]:
            currStart, currEnd = stack[-1]

            if currEnd < start:
                stack.append([start, end])
            elif currEnd >= start:
                new = [currStart, max(end, currEnd)]
                stack[-1] = new

        return stack
