# https://leetcode.com/problems/last-stone-weight/description/
# Key word: k-th largest, k-th smallest, heap


# 11 March 2025 Practice
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
                stones.sort()

        result = stones[0] if stones != [] else None

        return 0 if result is None else result


import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 == stone2:
                continue
            else:
                diff = abs(stone1 - stone2) * -1
                heapq.heappush(stones, diff)

        if stones:
            return stones[0] * -1
        else:
            return 0


# Example:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

s = Solution()
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1)
