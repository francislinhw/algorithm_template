# https://leetcode.com/problems/valid-anagram/

from typing import List


class Solution:
    # 27 Feb 2025 practice
    def isAnagram(self, s: str, t: str) -> bool:
        # 3.51

        def encode(words: str) -> List[int]:
            a = ord("a")

            result = [0 for i in range(26)]

            for char in words:
                ordChar = ord(char)
                result[ordChar - a] += 1

            return result

        sEncode = encode(s)
        tEncode = encode(t)

        return sEncode == tEncode
        # 3.55

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        # else is not prefferred

        hash_map_s = {}
        hash_map_t = {}

        def create_hash_map(s, map):
            for char in s:
                if char in map:
                    map[char] += 1
                    continue

                map[char] = 1

        create_hash_map(s, hash_map_s)
        create_hash_map(t, hash_map_t)

        if hash_map_s == hash_map_t:
            return True
        return False
