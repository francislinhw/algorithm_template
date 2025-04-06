# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict


# 4 Apr 2025 practice
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # use hashmap to record endode

        # Use a defaultdict to simplify the code
        def get_character_count_key(string):
            result = [0] * 26  # List for character counts
            aNum = ord("a")
            for char in string:
                index = ord(char.lower()) - aNum
                result[index] += 1
            return tuple(result)  # Convert list to tuple to make it hashable

        anagram_map = defaultdict(list)  # Default dict simplifies appending to lists

        for word in strs:
            key = get_character_count_key(word)  # Get encoded form of the word
            anagram_map[key].append(word)  # Append word to the list in anagram_map

        return list(
            anagram_map.values()
        )  # Return the grouped anagrams as a list of lists


# 4 Apr 2025 practice
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # use hashmap to record endode

        def encode(string):
            result = [0 for i in range(26)]
            aNum = ord("a")
            for char in string:
                # change char to lower case
                char = char.lower()
                index = ord(char) - aNum
                result[index] += 1
            return tuple(result)

        anagramMap = dict()

        for word in strs:
            code = encode(word)
            if code not in anagramMap:
                anagramMap[code] = []
            anagramMap[code].append(word)

        res = []

        for key, words in anagramMap.items():
            res.append(words)

        return res


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
