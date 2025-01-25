# https://leetcode.com/problems/insert-interval/description/

from typing import List


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
