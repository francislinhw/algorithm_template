# https://leetcode.com/problems/word-break/

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
        
        dp = [False] * (len(s)+1)
        dp[-1] = True

        for i in reversed(range(len(s))):
            for w in wordDict:
                if len(w) + i <= len(s):
                    currWord = s[i:i+len(w)]
                    if currWord in wordDict and dp[i + len(w)]:
                        dp[i] = True
        return dp[0]

        