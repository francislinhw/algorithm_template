# https://leetcode.com/problems/group-anagrams/
# class Solution:
#    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# charCnt = [0] * 26
# s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
# for char in s:
#     charCnt[ord(char) - ord('a')] += 1

# print(charCnt)

# Method 1
# def encodeWord(word: str):
#     charMap = {}
#     for char in word:
#         if char not in charMap:
#             charMap[char] = 0
#         charMap[char] += 1
#     charMap = dict(sorted(charMap.items()))
#     string = ''
#     for key, number in charMap.items():
#         string = string + str(number) + str(key)

#     return string

# resultDict = {}
# for s in strs:
#     pattern = encodeWord(s)
#     if pattern not in resultDict:
#         resultDict[pattern] = []
#     resultDict[pattern].append(s)

# returnlist = []

# for p, l in resultDict.items():
#     returnlist.append(l)

# print(resultDict)

# return returnlist

from typing import List


# 10 March 2025 practice
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 11.47

        def encode(word) -> List[int]:
            result = [0 for i in range(27)]
            base = ord("a") - 1

            for char in word:
                index = ord(char) - base
                result[index] += 1

            return result

        hashMap = {}

        for word in strs:
            code = tuple(encode(word))
            if code not in hashMap:
                hashMap[code] = []
            hashMap[code].append(word)

        res = []

        for i, lis in hashMap.items():
            res.append(lis)

        return res  # 11.58 10 min


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return []

        res = []
        charMap = {}

        for s in strs:
            charCnt = [0] * 26
            for char in s:
                charCnt[ord(char) - ord("a")] += 1
            charMapKey = tuple(charCnt)
            if charMapKey not in charMap:
                charMap[charMapKey] = []
            charMap[charMapKey].append(s)

        for anagramGrop in charMap.values():
            res.append(anagramGrop)

        return res
