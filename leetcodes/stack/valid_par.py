# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # stack = arr in python list
        pDict = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
                continue
            if not stack:
                return False
            matchingP = stack.pop()
            if pDict[char] != matchingP:
                return False
        return True if not stack else False

        # stack == [] == not stack


# March 1 2025 practice


class Solution:
    def isValid(self, s: str) -> bool:
        # 10.59
        stack = []
        rightParetheses = [")", "]", "}"]
        leftParetheses = ["(", "[", "{"]

        corespondingMap = {")": "(", "]": "[", "}": "{"}

        for p in s:
            if p in leftParetheses:
                stack.append(p)
            else:
                if stack == []:
                    return False
                cap = stack.pop()
                if cap != corespondingMap[p]:
                    return False

        if stack != []:
            return False

        return True
        # 104

        # 1035
        # dict {"(": True or False}

        # condition: if no ( , [, { in dict, but encounter ), ], }, then False
        # paMap = {}

        # rightParetheses = [")", "]", "}"]
        # leftParetheses = ["(", "[", "{"]

        # corespondingMap = {
        #     ")": "(",
        #     "]": "[",
        #     "}": "{"
        # }

        # for i in leftParetheses:
        #     paMap[i] = 0

        # for i in s:
        #     if i == rightParetheses[0] and paMap[leftParetheses[0]] == 0:
        #         return False

        #     if i == rightParetheses[1] and paMap[leftParetheses[1]] == 0:
        #         return False

        #     if i == rightParetheses[2] and paMap[leftParetheses[2]] == 0:
        #         return False

        #     if i in leftParetheses:
        #         paMap[i] += 1

        #     elif i in rightParetheses:
        #         paMap[corespondingMap[i]] -= 1

        # total = 0

        # for key, value in paMap.items():
        #     total = total + value

        # return True if total == 0 else False
