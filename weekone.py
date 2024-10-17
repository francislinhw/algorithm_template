list_one = [1, 2, 3, 4, 5]

dict_one = {
    "name": "John",
}

set_one = set()  # lookup is constant time O(1) (worse), Theta is average time complexity


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # set_nums = set(nums) # O(n) is from this.
        #
        # if len(set_nums) != len(nums):
        #    return True
        # else:
        #    return False

        # Standard solution
        set_nums = set()

        for n in nums:
            if n in set_nums:
                return True

            set_nums.add(n)

        return False

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        # else is not prefferred

        hash_map_s = {}
        hash_map_t = {}

        def create_hash_map(s, map):
            for char in s:
                if char in map:
                    map[char] += 1
                    continue

                map[char] = 1

        create_hash_map(s, hash_map_s)
        create_hash_map(t, hash_map_t)

        if hash_map_s == hash_map_t:
            return True
        return False

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # O(1)
        # array 8, 16 bite for one position, but string
        # O(n)
        pString = ""
        for char in s:
            if not char.isalnum():
                continue
            pString += char.lower()

        lPtr = 0
        rPtr = len(pString) - 1

        while lPtr < rPtr:
            leftChar = pString[lPtr]
            rightChar = pString[rPtr]

            if leftChar != rightChar:
                return False

            lPtr += 1
            rPtr -= 1

        return True

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        leftPtr = 0
        rightPtr = 0
        profit = 0

        while rightPtr < len(prices):
            if prices[leftPtr] > prices[rightPtr]:
                leftPtr = rightPtr  # template

            profit = max(prices[rightPtr] - prices[leftPtr], profit)
            rightPtr += 1  # template

        return profit

    # practice
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        newArr = arr

        for i in range(len(arr)):

            if i == len(arr) - 1:
                newArr[i] = -1
            else:
                newArr[i] = max(arr[i + 1 :])
        return newArr

        # Time complexity is O(n)
        # Sapce compelxity is O(n)

        # so I need to use space to earn time.

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # numsPositionHash = {}
        # for i in range(len(nums)):
        #     numsPositionHash[nums[i]] = i
        #
        # nums.sort()
        #
        # lPtr = 0
        # rPtr = len(nums) - 1
        #
        # while lPtr < rPtr:
        #     if nums[lPtr] + nums[rPtr] > target:
        #         rPtr -= 1
        #     elif  nums[lPtr] + nums[rPtr] < target:
        #         lPtr += 1
        #     else:
        #         if numsPositionHash[nums[lPtr]] == numsPositionHash[nums[rPtr]]:
        #             return [numsPositionHash[nums[lPtr]]-1, numsPositionHash[nums[rPtr]]]
        #         return [numsPositionHash[nums[lPtr]], numsPositionHash[nums[rPtr]]]

        newToOldIndexMap = {}

        for i in range(len(nums)):
            newToOldIndexMap[i] = i

        while True:
            hasExchange = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    temp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = temp
                    newToOldIndexMap[i] = i + 1
                    newToOldIndexMap[i + 1] = i
                    hasExchange = True

            if hasExchange == False:
                break

            hasExchange = False

        lPtr = 0
        rPtr = len(nums) - 1

        while lPtr < rPtr:
            if nums[lPtr] + nums[rPtr] > target:
                rPtr -= 1
            elif nums[lPtr] + nums[rPtr] < target:
                lPtr += 1
            else:
                return [newToOldIndexMap[lPtr], newToOldIndexMap[rPtr]]

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        returnS = s

        lPtr = 0
        rPtr = len(s) - 1

        while lPtr < rPtr:
            returnS[lPtr] = s[rPtr]
            returnS[rPtr] = s[lPtr]

        return returnS

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        lPtr = 0
        rPtr = 0

        length = 0

        while rPtr < len(s) - 1:
            if s[rPtr] in s[lPtr:rPtr]:
                lPtr += 1
            else:
                rPtr += 1
            maxLength = max(rPtr - lPtr, length)

        return maxLength

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lPtr = 0
        rPtr = 0

        length = 0

        while rPtr < len(s) - 1:
            if s[rPtr] in s[lPtr:rPtr]:
                lPtr += 1
            else:
                rPtr += 1
            maxLength = max(rPtr - lPtr, length)

        return maxLength
