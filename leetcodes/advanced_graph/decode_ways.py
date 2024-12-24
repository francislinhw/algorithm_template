# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == '0':
            return 0
        
        oneBack = 1 if int(s[-1]) != 0 else 0
        twoBack = 1

        for i in reversed(range(len(s)-1)):
            curr = 0
            if s[i] == '0':
                twoBack = oneBack
                oneBack = curr
                continue
            curr = oneBack

            doubleDig = int(s[i:i+2])
            if 10 <= doubleDig <= 26:
                curr += twoBack
            twoBack = oneBack
            oneBack = curr
        return oneBack