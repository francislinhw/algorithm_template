# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    # 26 Feb 2-25 daily challenge
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 8.05
        if not s:
            return 0

        # Step 1: For loop the string with variables (counting # of non-repeating char, max to record the history)
        maxHistory = 0
        currentCount = 0

        wordMap = {}  # (times, index)

        r = 0

        # for char in s:
        while r < len(s):
            char = s[r]
            # init
            if char not in wordMap:
                wordMap[char] = [0, 0]
            # main logic
            wordMap[char][0] += 1

            if wordMap[char][0] > 1:
                # duplicate
                index = wordMap[char][1]
                currentCount = 0
                wordMap = {}
                r = index + 1
            else:
                currentCount += 1
                wordMap[char][1] = r
                r += 1
            maxHistory = max(maxHistory, currentCount)

        return maxHistory  # 813 -> 833

    # Standard solution Best Time Complexity
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lPtr = 0
        rPtr = 0

        length = 0

        while rPtr < len(s) - 1:
            if s[rPtr] in s[lPtr:rPtr]:
                lPtr += 1
            else:
                rPtr += 1
            maxLength = max(rPtr - lPtr, length)

        return maxLength

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        setOne = set()

        lPtr = 0
        rPtr = 0

        length = 0

        while rPtr < len(s):
            # base case - trees graph
            while s[rPtr] in setOne:
                setOne.remove(s[lPtr])
                lPtr += 1

            setOne.add(s[rPtr])
            length = max(len(setOne), length)
            rPtr += 1

        return length

        # space O(1) because alphabet only has 26 chars.
