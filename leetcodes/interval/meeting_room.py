# https://www.lintcode.com/problem/920/


from typing import (
    List,
)

"""
Definition of Interval:
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# 9 March 2025 practice
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here

        intervalsList = []

        for interval in intervals:
            start = interval.start
            end = interval.end
            intervalsList.append([start, end])

        intervalsList.sort()

        prevEnd = None

        for interval in intervalsList:
            start = interval[0]
            end = interval[1]
            if prevEnd is None:
                prevEnd = end
            else:
                if start < prevEnd:
                    return False
                prevEnd = max(end, prevEnd)
        return True


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # # Write your code here
        # intervals.sort(key = lambda x: x.start)
        # stack = []
        # stack.append(intervals[0])

        # for start, end in intervals[1:]:
        #     currStart, currEnd = stack[-1]

        #     if currEnd < start:
        #         stack.append([start, end])
        #     elif currEnd >= start:
        #         new = [currStart, max(end, currEnd)]
        #         stack[-1] = new
        #         return False

        # return True
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        lastEnd = intervals[0].end

        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end

            if start < lastEnd:
                return False
            else:
                lastEnd = max(end, lastEnd)
        return True
