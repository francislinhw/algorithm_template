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


# March 2 2025 practice


class Solution:
    def sortArray(self, nums):
        # 1113
        # Divide and conquer

        def conquer(groupA, groupB):
            comb = []
            i = 0
            j = 0

            while (
                groupB is not None
                and groupA is not None
                and i < len(groupA)
                and j < len(groupB)
            ):
                numbA = groupA[i]
                numbB = groupB[j]

                if numbA < numbB:
                    comb.append(numbA)
                    i += 1

                elif numbB < numbA:
                    comb.append(numbB)
                    j += 1
                else:
                    comb.append(numbA)
                    comb.append(numbB)
                    j += 1
                    i += 1

            while groupA is not None and i < len(groupA):
                comb.append(groupA[i])
                i += 1

            while groupB is not None and j < len(groupB):
                comb.append(groupB[j])
                j += 1

            return comb

        def divide(group):
            if len(group) <= 1:
                return group
            length = len(group)
            mid = max((length - 1) // 2, 1)
            print(mid)
            groupA = group[0:mid]
            groupB = group[mid:]
            if len(groupA) >= 2:
                leftArr = divide(groupA)
            else:
                leftArr = groupA
            if len(groupB) >= 2:
                rightArr = divide(groupB)
            else:
                rightArr = groupB
            result = conquer(leftArr, rightArr)
            return result

        result = divide(nums)

        return result
        # 1140 30 min
