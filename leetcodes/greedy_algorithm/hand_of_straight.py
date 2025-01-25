# https://leetcode.com/problems/hand-of-straights/submissions/1507874035/

from typing import List
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # min heap
        # build min heap O(n) +

        if len(hand) % groupSize:
            return False

        cnt = {}
        for num in hand:
            if num not in cnt:
                cnt[num] = 1
                continue
            cnt[num] += 1

        handHeap = list(set(hand))
        heapq.heapify(handHeap)

        while handHeap:
            firstNum = handHeap[0]
            for j in range(firstNum, firstNum + groupSize):
                if j not in cnt or cnt[j] == 0:
                    return False
                cnt[j] -= 1
                # if j cnt[j] == 0 we need to check if it is the smallest ele in heap
                # or else there will be a gap
                if cnt[j] == 0:
                    if j != handHeap[0]:  # current number is not the min
                        return False
                    heapq.heappop(handHeap)
        return True
