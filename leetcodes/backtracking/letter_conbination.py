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

            for j in range(len(digitsMap[digits[i]])):
                tmp.append(digitsMap[digits[i]][j])
                backtrack(i + 1)
                tmp.pop()

        backtrack(0)
        return res
