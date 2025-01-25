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


# https://www.lintcode.com/problem/919
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([j.end for j in intervals])
        cnt = 0
        res = 0

        sPtr = 0
        cPtr = 0

        while sPtr < len(start):
            if start[sPtr] < end[cPtr]:
                cnt += 1
                sPtr += 1
            else:
                cnt -= 1
                cPtr += 1
            res = max(cnt, res)
        return res
