# https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt = 0
        mostRecentEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # if mostRecentEnd > start:
            #     cnt += 1
            #     mostRecentEnd = min(mostRecentEnd, end)
            if start >= mostRecentEnd:
                mostRecentEnd = end
            else:
                cnt += 1
                mostRecentEnd = min(mostRecentEnd, end)

        return cnt
