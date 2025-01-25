# time complexity: O(nlogn)
# space complexity: O(n)
# average time complexity: O(nlogn)
# divide and conquer

# concept: in the middle of the array, split the array into two halves, and then sort each half, and then merge the two halves


# https://leetcode.com/problems/sort-an-array/
# https://codeshare.io/VNB7rQ
class Solution:
    def sortArray(self, nums):

        def conquer(leftArr, rightArr):
            comb = []
            i = 0
            j = 0

            while i < len(leftArr) and j < len(rightArr):
                leftVal = leftArr[i]
                rightVal = rightArr[j]
                if leftVal <= rightVal:
                    comb.append(leftVal)
                    i += 1
                else:
                    comb.append(rightVal)
                    j += 1

            while i < len(leftArr):
                leftVal = leftArr[i]
                comb.append(leftVal)
                i += 1

            while j < len(rightArr):
                rightVal = rightArr[j]
                comb.append(rightVal)
                j += 1
            return comb

        def divide(arr):
            if len(arr) <= 1:
                return arr

            l = 0
            r = len(arr)
            mid = (l + r) // 2
            leftArr = divide(arr[:mid])
            rightArr = divide(arr[mid:])
            combArr = conquer(leftArr, rightArr)
            return combArr

        return divide(nums)


# ******** Example ******** #

solution = Solution()
nums = [1, 3, 5, 7, 2, 4, 6, 8]
print(solution.sortArray(nums))
