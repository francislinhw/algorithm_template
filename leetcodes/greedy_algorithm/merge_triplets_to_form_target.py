# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

from typing import List


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
