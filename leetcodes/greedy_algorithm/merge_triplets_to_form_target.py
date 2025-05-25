# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        p = [False, False, False]

        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    if triplet[i] == target[i]:
                        p[i] = True

        return all(p)


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 10.22
        p = [False, False, False]

        for i in range(3):  # 0 1 2
            for j in range(len(triplets)):
                triplet = triplets[j]
                other1Index = (i + 1) % 3  # 1 2 0
                other2Index = (i + 2) % 3  # 2 0 1

                if (
                    triplet[i] == target[i]
                    and triplet[other1Index] <= target[other1Index]
                    and triplet[other2Index] <= target[other2Index]
                ):
                    p[i] = True

        return p[0] and p[1] and p[2]  # 30 min


# 13 March 2025
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 9.39
        valid_triplets = set()

        for triplet in triplets:
            # 只保留所有元素 <= target 的 triplet
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    if triplet[i] == target[i]:
                        valid_triplets.add(i)

        # 確保 target 的每個元素都能被至少一個 triplet 覆蓋
        return len(valid_triplets) == 3
        # 9.53


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


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        seenIdx = set()

        # 檢查 triplet 是否有元素超過 target，若是則無法選擇
        def isInvalidTriplet(triplet):
            return any(triplet[i] > target[i] for i in range(3))

        # 追蹤 target 中哪些索引已經被滿足
        def markMatchingIndices(triplet):
            for i in range(3):
                if triplet[i] == target[i]:
                    seenIdx.add(i)

        # 遍歷所有 triplets，篩選可用的並記錄匹配索引
        for triplet in triplets:
            if isInvalidTriplet(triplet):
                continue
            markMatchingIndices(triplet)

        # 必須覆蓋 target 的所有索引（0,1,2）
        return len(seenIdx) == 3
