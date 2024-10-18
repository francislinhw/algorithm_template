# linked List

from collections import deque


class Node(object):
    def __init__(self, left=None, right=None, value=None):
        left = None
        right = None


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


def dfs(node):
    if node is None:
        return None
    dfs(node.left)
    dfs(node.right)

    # deck is pop_left and pop_right (deque)

    # DFS:
    def dfs(self, root):
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

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # not O(n), must sorted, the fastest O(log(n))

        lPtr = 0
        rPtr = len(nums) - 1

        while rPtr >= lPtr:
            midPtr = (rPtr + lPtr) // 2
            if nums[midPtr] == target:
                countIndex = midPtr
                returnPtr = midPtr
                while countIndex >= 0:
                    if nums[countIndex] == target:
                        returnPtr = countIndex
                        countIndex -= 1
                    else:
                        break
                return returnPtr

            elif target > nums[midPtr]:
                lPtr = midPtr + 1
            else:
                rPtr = midPtr - 1

        return lPtr

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # sorted -> binary
        # reverse a lined list

        # not O(n), must sorted, the fastest O(log(n))

        # uPtr = 0
        # dPtr = len(matrix) - 1
        #
        # while dPtr >= uPtr:  # could be overlap
        #
        #    if uPtr == dPtr:
        #        lPtr = 0
        #        rPtr = len(matrix[uPtr]) - 1
        #
        #        while rPtr >= lPtr:  # could be overlap
        #            imidPtr = (rPtr + lPtr) // 2  # integer division
        #            if matrix[uPtr][imidPtr] == target:
        #                return True
        #
        #            elif target > matrix[uPtr][imidPtr]:
        #                lPtr = imidPtr + 1
        #            else:
        #                rPtr = imidPtr - 1
        #
        #        return False
        #
        #    midPtr = (dPtr + uPtr) // 2  # integer division
        #    if matrix[midPtr][0] == target or matrix[midPtr][-1] == target:
        #        return True
        #
        #    elif matrix[midPtr][0] < target and matrix[midPtr][-1] > target:
        #        uPtr = midPtr
        #        dPtr = midPtr
        #
        #    elif matrix[midPtr][0] < target and matrix[midPtr][-1] < target :
        #        uPtr = midPtr + 1
        #    else:
        #        dPtr = midPtr - 1
        #

        t = 0
        b = len(matrix) - 1

        def bSearch(row):
            l = 0
            r = len(matrix[row]) - 1

            while l <= r:
                m = (l + r) // 2
                if matrix[row][m] > target:
                    r = m - 1
                elif matrix[row][m] < target:
                    l = m + 1
                else:
                    return True
            return False

        while t <= b:
            m = (t + b) // 2
            if target > matrix[m][-1]:
                t = m + 1
            elif target < matrix[m][0]:
                b = m - 1
            else:
                return bSearch(m)
        return False
