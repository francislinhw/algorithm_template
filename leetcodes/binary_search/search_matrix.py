from typing import List

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
