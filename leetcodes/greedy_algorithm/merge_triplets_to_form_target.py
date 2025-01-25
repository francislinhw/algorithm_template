# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        seenIdx = set()

        def missMatch(triplet):
            for i in range(len(triplet)):
                if triplet[i] > target[i]:
                    return True
            return False

        def matching(triplet):
            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    seenIdx.add(i)

        for triplet in triplets:
            if missMatch(triplet):
                continue
            matching(triplet)
        return len(seenIdx) == len(target)
