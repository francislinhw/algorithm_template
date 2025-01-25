# https://leetcode.com/problems/product-of-array-except-self/description/

# class Solution:
#    def productExceptSelf(self, nums: List[int]) -> List[int]:
# res = []

# cacheMap = {}

# # O(n) * 3 O(n) = O(n^2)
# for i in range(len(nums)):
#     currentProduct = 1
#     sublist = nums[:i] + nums[(i + 1):] # 2 * O(n)
#     subTuple = tuple(sublist)
#     if subTuple in cacheMap:
#         currentProduct = cacheMap[subTuple]
#     else:
#         for j in range(len(sublist)): # 1 O(n)
#             currentProduct *= sublist[j]
#         cacheMap[subTuple] = currentProduct

#     res.append(currentProduct)

# print(cacheMap)


# return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # [1, 1, 2, 6]
        postfix = 1
        for j in reversed(range(len(nums))):
            res[j] *= postfix
            postfix *= nums[j]
        return res
