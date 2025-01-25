    def isValid(self, s):
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