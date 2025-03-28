# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res = []
        tmp = []
        digitsMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(i):
            if i == len(digits):
                ans = "".join(tmp.copy())
                res.append(ans)
                return

            currentDigit = digits[i]

            for j in range(len(digitsMap[currentDigit])):
                tmp.append(digitsMap[currentDigit][j])
                backtrack(i + 1)
                tmp.pop()

        backtrack(0)
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is None or digits == "":
            return []

        res = []
        currPerm = ""

        phoneTable = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "0": [],
        }

        def dfs(index, currPerm):
            if len(digits) == len(currPerm):
                res.append(currPerm)

            if index > len(digits) - 1:
                return

            number = digits[index]

            for char in phoneTable[
                number
            ].copy():  # copy to let the below operation to not having changes to loops
                currPerm = currPerm + char
                # phoneTable[number].remove(char) # add if not allow duplication
                dfs(index + 1, currPerm)
                currPerm = currPerm[:-1]
                # phoneTable[number].append(char) # add if not allow duplication

        index = 0
        dfs(index, currPerm)
        return res
