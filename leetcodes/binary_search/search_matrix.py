from typing import List


# 17 March 2025 Practice
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 10.08
        if target < matrix[0][0]:
            return False
        if target > matrix[-1][-1]:
            return False

        def BinarySearch(target, nums) -> bool:
            l = 0
            r = len(nums) - 1

            while l <= r:
                left = nums[l]
                right = nums[r]
                mid = (l + r) // 2
                middle = nums[mid]
                print(left)
                print(right)
                print(middle)

                if left == target or right == target or target == middle:
                    return True
                elif target > middle:
                    l = mid + 1
                elif target < middle:
                    r = mid - 1

            return False

        numberOfRow = 0

        for elements in matrix:
            if target <= elements[-1]:
                break
            elif target > elements[-1]:
                numberOfRow += 1

        return BinarySearch(target, matrix[numberOfRow])  # 21 Min


# 4th March 2025 Practice


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 7.37

        def binarySearchRow(target, searchRange):
            if len(searchRange) == 1:
                return 0
            if target < searchRange[1]:
                return 0
            if target > searchRange[-1]:
                return len(searchRange) - 1

            l = 0
            r = len(searchRange) - 1

            while l <= r:
                mid = (l + r) // 2
                print("mid", mid)
                middleLess = searchRange[max(0, mid - 1)]
                middle = searchRange[mid]
                middleMore = searchRange[min(len(searchRange) - 1, mid + 1)]

                if middle == target:
                    return mid
                elif middle <= target and target < middleMore:
                    return mid
                elif middle > target and target >= middleLess:
                    return max(0, mid - 1)
                elif middle < target:
                    l = mid + 1
                elif middle > target:
                    r = mid - 1

        def binarySearch(target, searchRange):
            l = 0
            r = len(searchRange) - 1

            while l <= r:
                mid = (l + r) // 2
                print("mid2", mid)
                middle = searchRange[mid]

                if middle == target:
                    return True
                elif middle < target:
                    l = mid + 1
                elif middle > target:
                    r = mid - 1

            return False

        rows = [x[0] for x in matrix]
        print(rows)

        tRow = binarySearchRow(target, rows)
        print(tRow)
        return binarySearch(target, matrix[tRow])
        # 8.31 56 min

    # Standard

    # Time complexity is O(n)
    # Sapce compelxity is O(1) (input, output, in progress)

    # so I need to use space to earn time.

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
