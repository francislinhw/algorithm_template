# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 指標設在 nums1 和 nums2 的尾端，以及合併結果的尾端
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 若 nums2 還有剩，把它們補上去（nums1 剩下的不需動，已在正確位置）
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
