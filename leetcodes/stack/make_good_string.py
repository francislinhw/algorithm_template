# https://leetcode.com/problems/make-the-string-great/


class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def toString(self):
        return "".join(self.stack)


class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        sStack = Stack()

        def checkCondition(s1, s2):
            if s1 == None or s2 == None:
                return False
            return s1.upper() == s2.upper() and s1 != s2
            # return s1.lower() == s2.lower() and s1 == s2.lower() and s1.upper() == s2

        for char in s:
            if sStack and checkCondition(sStack.top(), char):
                sStack.pop()
            else:
                sStack.push(char)  # space complexity O(n)

        return sStack.toString()


# March 1 2025 Practice


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            # 如果 stack 不為空，且當前字母與 stack 最上層元素形成大小寫對應
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()  # 刪除上一個字母，表示這兩個字母被移除
            else:
                stack.append(char)  # 否則將當前字母加入 stack

        return "".join(stack)
