# https://leetcode.com/problems/merge-intervals/

from typing import List


# 10 March 2025
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 12.00
        intervals.sort()

        newInterval = [[intervals[0][0], intervals[0][1]]]

        for interval in intervals:
            low = interval[0]
            high = interval[1]

            if low > newInterval[-1][1]:
                newInterval.append([low, high])
            elif low <= newInterval[-1][1]:
                if high > newInterval[-1][1]:
                    newInterval[-1][1] = high

        return newInterval  # 12.09


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
