
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



class Solution:
    # graph: backtraking dynamic programming: dfs or bfs

    # depth first search or breadth first search
    # time complexity: O(n) - n is the number of nodes
    # recurrsion hight of the tree O(H)

    # depth first search: go to the deepest node first and then backtrack
    # breadth first search: go to the next level first and then go to the next level

    # time complexity: O(n) - n is the number of nodes
    # space complexity: O(n) - n is the number of nodes
    # binary search tree / binary tree # 99% left is first and right is second
    # O(2n -1)

    # time complexity: O(n) - n is the number of nodes

    # binary search tree / binary tree # 99% left is first and right is second

    def dfs(self, node):
        if node is None:
            return None
        self.dfs(node.left)
        self.dfs(node.right)

    # deck is pop_left and pop_right (deque)

    # DFS:
    def invertTree(self, root):
        if not root:
            return None

        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root

        # O(N) time, space O(H) height of the tree

    # BFS:
    def bfs(self, root):
        depth = 0
        if not root:
            return depth
        q = deque()
        q.append(root)

        while q:
            depth += 1
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                if node.left or node.right:
                    q.append(node.left)
                    q.append(node.right)
        return depth

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = 0
        res = float("-inf")
        currSum = 0
        listOne = [0, 0]
        while r < len(nums):
            currSum += nums[r]

            if currSum > res:
                listOne = [l, r]
                res = currSum

                # res = max(res, currSum)
            if currSum >= 0:
                r += 1
            else:
                r += 1
                l = r
                currSum = 0
        return res


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
