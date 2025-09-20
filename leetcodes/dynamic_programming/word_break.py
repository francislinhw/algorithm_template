# https://leetcode.com/problems/word-break/
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if s.startswith(w, i):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 3.10
        dp = [False] * (len(s))
        dp.append(True)

        for i in reversed(range(len(s))):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w and dp[i + len(w)]:
                    dp[i] = True
                    break

        return dp[0]


# 14 April 2025
class Solution(object):  # Top-down
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 8.06
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True  # 空字串視為可分割
        for i in reversed(range(len(s))):  # 從右往左掃
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet and dp[j]:
                    dp[i] = True
                    break  # 一旦成立就不用再試
        return dp[0]


class Solution(object):  # Bottom-up
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)  # O(1) 查詢效率
        dp = [False] * (len(s) + 1)
        dp[0] = True  # 空字串可以被切割

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]


# class Solution:
# def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#     if not s or not wordDict:
#         return False

#     positionMark = [False] * len(s) # +1

#     for i in range(1, len(s) + 1):
#         for wordIndex in reversed(range(i - 1, len(s))):
#             word = s[wordIndex + 1 - i:wordIndex + 1]
#             if word in wordDict and positionMark[i + len(word)] != False:
#                 positionMark[wordIndex - i + 1] = [True, len(word)]

#     print(positionMark)

#     pointer = positionMark[0]
#     accuIndex = 0

#     while pointer is not None:
#         print(pointer)
#         if pointer == False:
#             return False

#         valid = pointer[0]

#         if not valid:
#             return False

#         nextIndex = pointer[1]
#         accuIndex = accuIndex + nextIndex
#         print(accuIndex)

#         if accuIndex <= len(positionMark) - 1:
#              pointer = positionMark[accuIndex]
#         else:
#             pointer = None
#             if accuIndex > len(positionMark):
#                 return False

#     return True

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in reversed(range(len(s))):
            for w in wordDict:
                if len(w) + i <= len(s):
                    currWord = s[i : i + len(w)]
                    if currWord in wordDict and dp[i + len(w)]:
                        dp[i] = True
        return dp[0]
