# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

import heapq


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
