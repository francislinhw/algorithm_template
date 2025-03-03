# https://leetcode.com/problems/min-stack/

# March 1 2025 Practice


class MinStack:
    # 11.32

    def __init__(self):
        self.stack = []
        self.minStack = None  # min only

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack is None or self.minStack == []:
            self.minStack = [val]
        else:
            minVal = min(self.minStack[-1], val)
            self.minStack.append(minVal)

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# first


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            minVal = min(self.minStack[-1], val)
            self.minStack.append(minVal)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # edge case
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
