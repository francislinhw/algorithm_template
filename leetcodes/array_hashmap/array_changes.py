# https://leetcode.com/problems/replace-elements-in-an-array/
from typing import List


# 6 Apr 2025 practice
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        """使用哈希映射加速查找和更新，以提高執行效率"""
        # 11.12
        hashMap = {value: index for index, value in enumerate(nums)}

        for original, to in operations:
            oriIndex = hashMap[original]
            nums[oriIndex] = to
            del hashMap[original]
            hashMap[to] = oriIndex

        return nums


# 3 March 2025
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        """使用哈希映射加速查找和更新，以提高執行效率"""
        # 建立數值位置對應表：數值 -> nums 中的索引
        index_map = {num: i for i, num in enumerate(nums)}

        # 依序執行 operations
        for old_val, new_val in operations:  # 確保依序執行
            if old_val in index_map:  # 只處理存在於 nums 的數值
                index = index_map[old_val]  # 找到對應索引
                nums[index] = new_val  # 更新 nums 中的值
                del index_map[old_val]  # 移除舊值
                index_map[new_val] = index  # 記錄新值對應的索引

        return nums
