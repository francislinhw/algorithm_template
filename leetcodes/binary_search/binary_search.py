
class Solution:
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
