# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

import heapq
from typing import List

# 11 March 2025 Practice
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # 8.35
        newNums = []

        for i in nums:
            newNums.append(int(i))
        
        heapq.heapify(newNums)

        while len(newNums) > k:
            a = heapq.heappop(newNums)

        result = str(heapq.heappop(newNums))
        
        return result
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """

        if not nums or not k:
            return None

        if len(nums) < k:
            return None

        numsInt = [int(number) for number in nums]

        heapq.heapify(numsInt)

        # target = (len(nums) - 1) - (k - 1)
        kLargest = None

        for i in range(k):
            kLargest = heapq.heappop(numsInt)  # 不要用sort的想法寫
            # if i == target:
            #  return str(kLargest)
        return str(kLargest)
    

# Quick selection Algorithm

def findKthLargest(nums: List, k: int) -> int:
    sizeN = len(nums)
    l = 0
    r = sizeN

    while l < r:
        i = l
        j = r - 1
        pivot = nums[l]
        while i <= j:
            while i <= j and nums[i] >= pivot:
                i += 1
            while i <= j and nums[i] < pivot:
                j -= 1
            if i < j:
                swap(nums[i++], nums[j--])
        swap(nums[left], nums[j])
        if j == k -1:
            return nums[j]
        if j < k - 1:
            left = j + 1
        else:
            right = j




