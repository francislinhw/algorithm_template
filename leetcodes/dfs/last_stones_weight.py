# https://leetcode.com/problems/last-stone-weight/

from typing import List
from heapq import heapify, heappop, heappush


# 22 March 2025
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 5.33
        if not stones:
            return 0

        # Python 預設是最小堆，我們要模擬最大堆，可以先把所有數字取負值
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            m1 = -heappop(stones)
            m2 = -heappop(stones)
            if m1 != m2:
                heappush(stones, -(m1 - m2))

        return -stones[0] if stones else 0


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 6.58
        stones.sort()

        def crash(left, right) -> int | None:
            if left != right:
                return abs(right - left)
            else:
                return None

        result = 0

        while len(stones) > 1:
            right = stones.pop()
            left = stones.pop()
            res = crash(left, right)
            if res is not None:
                stones.append(res)
                stones.sort()  # time complexity: O(nlogn) is really slow, using heap is better

        result = stones[0] if stones != [] else None

        return 0 if result is None else result
