# https://leetcode.com/problems/palindromic-substrings/description/
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 11.10 string
        def isPalindromic(string):
            return string == string[::-1]

        count = [0]
        res = [set()]

        def dfs(start, num):
            if start + num > len(s):
                return
            subres = s[start : start + num]
            if subres not in res[0] and isPalindromic(subres):
                count[0] += 1
            dfs(start + 1, num)

        for i in range(1, len(s) + 1):
            dfs(0, i)

        return count[0]  # 11.22


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def extend(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        total = 0
        for i in range(len(s)):
            total += extend(i, i)  # 奇數長度回文（中心為一個字母）
            total += extend(i, i + 1)  # 偶數長度回文（中心為兩個字母）

        return total


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 0409 8.27

        # Step 1: I need a function to cal the substring of certain length -> ["a"]
        # Step 1: I also need to palidromic function
        def isPalindromic(w):
            l = 0
            r = len(w) - 1
            while l < r:
                left = w[l]
                right = w[r]
                if left != right:
                    return False
                l += 1
                r -= 1
            return True

        # Step 2: I need to iterate the sertain lenth and put in the function]

        # Step 3: return len(result)

        def qualifiedSubstring(s, length):
            res = []
            if length > len(s):
                return []
            for i in range(len(s) - length + 1):
                substring = s[i : i + length]
                if isPalindromic(substring):
                    res.append(substring)
            return res

        result = []
        for j in range(1, len(s) + 1):
            subres = qualifiedSubstring(s, j)
            result = result + subres
        print(result)

        return len(result)


class Solution:
    def countSubstrings(self, s: str) -> int:
        # def checkPalidromic(strig: str):
        #     l = 0
        #     r = len(string)

        #     isSame = True

        #     while l <= r:
        #         first = string[l]
        #         second = string[r]

        #         if first != second:
        #             isSame = False

        #         l += 1
        #         r -= 1

        #     return isSame

        self.cnt = 0

        def checkPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.cnt += 1
                l -= 1
                r += 1
            return

        for i in range(len(s)):
            l = i
            r = i
            checkPalindrome(l, r)
            l = i
            r = i + 1
            checkPalindrome(l, r)
        return self.cnt
