# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/description/
from collections import Counter


class Solution(object):
    def minDeletion(self, s, k):
        freq = Counter(s).values()  # 各字母出現次數
        most_common = sorted(freq, reverse=True)[:k]  # 保留出現最多的 k 種
        return sum(freq) - sum(most_common)  # 剩下的全刪


#         distinct = []
#         number = 0
#         for char in s:
#             if char not in distinct:
#                 distinct.append(char)
#                 number += 1

#         return max(0, number - k)
