# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:

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

    def isPalindrome(self, s: str) -> bool:
        to_remove = set(",.!?':;\"()[]{}<>-_=+*/\\|@#%^&~` ")
        filtered_chars = [char.lower() for char in s if char not in to_remove]
        return filtered_chars == filtered_chars[::-1]

    def isPalindrome(self, s: str) -> bool:
        a = ord("a")
        z = ord("z")
        A = ord("A")
        Z = ord("Z")
        zero = ord("0")
        nine = ord("9")

        filtered_chars = [
            char.lower()
            for char in s
            if (zero <= ord(char) <= nine)
            or (A <= ord(char) <= Z)
            or (a <= ord(char) <= z)
        ]
        return filtered_chars == filtered_chars[::-1]

    def isPalindrome(self, s: str) -> bool:
        filtered_chars = []

        for char in s:
            if ("0" <= char <= "9") or ("a" <= char <= "z") or ("A" <= char <= "Z"):
                filtered_chars.append(char.lower())  # 轉成小寫，忽略大小寫

        return filtered_chars == filtered_chars[::-1]  # 判斷是否為回文

    def isPalindrome(self, s: str) -> bool:
        to_remove = ",.!?':;\"()[]{}<>-_=+*/\\|@#%^&~` "  # 需要刪除的字符
        s = s.translate(str.maketrans("", "", to_remove))  # 移除不需要的字符
        # translate 是 python 的內建函數，用於替換字符串中的字符。
        # str.maketrans 用於創建一個字符映射表，將需要替換的字符映射為空字符串。
        # 這樣做的目的是將字符串中的所有需要刪除的字符都替換為空字符串，從而達到刪除這些字符的目的。
        s = s.lower()  # 忽略大小寫
        return s == s[::-1]  # 檢查是否為回文
