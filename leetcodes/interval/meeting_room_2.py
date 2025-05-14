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


from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # 依照開始時間排序
        intervals.sort(key=lambda x: x.start)

        # 使用最小堆來追蹤所有會議室的結束時間
        heap = []
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)):
            # 如果新的會議可以接在最早結束的會議之後，重用該會議室
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, intervals[i].end)

        return len(heap)


# https://www.lintcode.com/problem/919
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted(
            [j.end for j in intervals]
        )  # equivalent to end = [j.end for j in intervals].sort()
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
