# https://leetcode.com/problems/insert-interval/description/

from typing import List


# 10 March 2025 practice
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # 11.05
        intervals.append(newInterval)
        intervals.sort()

        newInverv = [[intervals[0][0], intervals[0][1]]]

        prevEnd = intervals[0][1]
        for start, end in intervals[1::]:
            if start <= prevEnd and end > prevEnd:
                newInverv[-1][1] = end
            elif start > prevEnd:
                newInverv.append([start, end])
            prevEnd = max(end, prevEnd)

        return newInverv  # 11.17 12 min


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):

            start = interval[0]
            end = interval[1]

            if newInterval[1] < start:  # 整串return
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end:  # 不可conbine
                res.append(interval)
            else:
                # conbine
                minVal = min(start, newInterval[0])
                maxVal = max(end, newInterval[1])
                newInterval = [minVal, maxVal]
        res.append(newInterval)
        return res
