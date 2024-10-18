class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # sorted -> binary
        # reverse a lined list

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # not O(n), must sorted, the fastest O(log(n))

        lPtr = 0
        rPtr = len(nums) - 1

        while rPtr >= lPtr:  # could be overlap
            midPtr = (rPtr + lPtr) // 2  # integer division
            if nums[midPtr] == target:
                return midPtr

            elif target > nums[midPtr]:
                lPtr = midPtr + 1
            else:
                rPtr = midPtr - 1

        return -1

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

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        setOne = set()

        lPtr = 0
        rPtr = 0

        length = 0

        while rPtr < len(s):
            # base case - trees graph
            while s[rPtr] in setOne:
                setOne.remove(s[lPtr])
                lPtr += 1

            setOne.add(s[rPtr])
            length = max(len(setOne), length)
            rPtr += 1

        return length

        # space O(1) because alphabet only has 26 chars.

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        # lPtr = 0
        # rPtr = len(s) - 1
        #
        # while lPtr < rPtr:
        #     left = s[rPtr]
        #     right = s[lPtr]
        #     s[lPtr] = left
        #     s[rPtr] = right
        #     lPtr += 1
        #     rPtr -= 1

        # Time complexity is O(n)
        # Sapce compelxity is O(1)
        l = 0
        r = len(s) - 1

        while r > l:
            s[l], s[r] = s[r], s[l]  # python only
            l += 1
            r -= 1
        return s

    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        greatestNum = float("-inf")

        # range(len(arr), -1, -1)

        for i in reversed(range(len(arr))):
            currNum = arr[i]
            arr[i] = greatestNum
            if currNum > greatestNum:
                greatestNum = currNum

        arr[-1] = -1
        return arr

        # Time complexity is O(n)
        # Sapce compelxity is O(1) (input, output, in progress)

        # so I need to use space to earn time.

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, val in enumerate(nums):
            if val in seen:
                return [idx, seen[val]]
            remain = target - val
            seen[remain] = idx

    # Practice
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # sorted -> binary
        # reverse a lined list

        # not O(n), must sorted, the fastest O(log(n))

        uPtr = 0
        dPtr = len(matrix) - 1

        while dPtr >= uPtr:  # could be overlap

            if uPtr == dPtr:
                lPtr = 0
                rPtr = len(matrix[uPtr]) - 1

                while rPtr >= lPtr:  # could be overlap
                    imidPtr = (rPtr + lPtr) // 2  # integer division
                    if matrix[uPtr][imidPtr] == target:
                        return True

                    elif target > matrix[uPtr][imidPtr]:
                        lPtr = imidPtr + 1
                    else:
                        rPtr = imidPtr - 1

                return False

            midPtr = (dPtr + uPtr) // 2  # integer division
            if matrix[midPtr][0] == target or matrix[midPtr][-1] == target:
                return True

            elif matrix[midPtr][0] < target and matrix[midPtr][-1] > target:
                uPtr = midPtr
                dPtr = midPtr

            elif matrix[midPtr][0] < target and matrix[midPtr][-1] < target:
                uPtr = midPtr + 1
            else:
                dPtr = midPtr - 1

        return False

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
