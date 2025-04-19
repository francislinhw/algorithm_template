# https://leetcode.com/problems/longest-palindromic-substring/description/


# 19 Apr 2025 Practice
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 3.08
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]  # 注意：因為 left/right 會多移動一次，所以要調整

        res = ""

        for i in range(len(s)):
            # 奇數長度的回文（中心是 i）
            temp1 = expandAroundCenter(i, i)
            # 偶數長度的回文（中心是 i 和 i+1）
            temp2 = expandAroundCenter(i, i + 1)

            # 取較長者更新結果
            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2

        return res


# Manacher's Algorithm
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. 前處理：加入特殊符號 '#'，用於統一處理奇數和偶數長度的回文子字串。
        #    例如，"aba" 變成 "#a#b#a#"，"abba" 變成 "#a#b#b#a#"。
        T = "#" + "#".join(s) + "#"
        n = len(T)
        # 2. P 陣列：P[i] 儲存以 T[i] 為中心的最長回文子字串的半徑長度（不包含 T[i] 本身）。
        P = [0] * n
        # 3. center：目前已知的最長回文子字串的中心在 T 中的索引。
        # 4. right：目前已知的最長回文子字串的右邊界索引，等於 center + P[center]。
        center = right = 0
        # 5. max_len：記錄找到的最長回文子字串的半徑長度。
        max_len = 0
        # 6. center_index：記錄最長回文子字串的中心在 T 中的索引。
        center_index = 0

        # 遍歷轉換後的字串 T
        for i in range(n):
            # 7. mirror：索引 i 關於當前回文中心 center 的對稱點。
            mirror = 2 * center - i

            # 8. 如果當前索引 i 在目前已知最長回文子字串的右邊界 right 內，
            #    則 P[i] 的初始值可以根據其對稱點 mirror 的 P[mirror] 和 i 到 right 的距離來確定。
            if i < right:
                # P[i] 的值是 P[mirror] 和 right - i 中的較小值。
                # 這利用了回文串的對稱性，避免重複計算。
                P[i] = min(right - i, P[mirror])

            # 9. 嘗試以 T[i] 為中心向外擴展回文子字串。
            a = i + P[i] + 1  # 右邊界下一個位置
            b = i - P[i] - 1  # 左邊界前一個位置
            # 只要左右兩邊都在 T 的有效範圍內，並且對應的字元相等，就繼續擴展。
            while a < n and b >= 0 and T[a] == T[b]:
                P[i] += 1  # 半徑增加 1
                a += 1  # 向右移動
                b -= 1  # 向左移動

            # 10. 如果以 T[i] 為中心的回文子字串的右邊界 i + P[i] 超出了目前已知的右邊界 right，
            #     則更新 center 為 i，並且更新 right 為新的右邊界。
            if i + P[i] > right:
                center = i
                right = i + P[i]

            # 11. 如果當前回文子字串的半徑 P[i] 大於目前找到的最長半徑 max_len，
            #     則更新 max_len 和 center_index。
            if P[i] > max_len:
                max_len = P[i]
                center_index = i

        # 12. 從轉換後的字串 T 中的最長回文子字串的中心索引 center_index 和半徑 max_len，
        #     計算出它在原始字串 s 中的起始位置 start。
        #     由於在 T 中每個原始字元之間都有一個 '#',
        #     所以原始字串中的長度就是 max_len。
        #     起始位置的計算需要將 T 中的索引轉換回 s 中的索引。
        start = (center_index - max_len) // 2
        # 13. 返回原始字串 s 中從 start 開始，長度為 max_len 的子字串，這就是最長的回文子字串。
        return s[start : start + max_len]


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 3.08
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]  # 注意：因為 left/right 會多移動一次，所以要調整

        res = ""

        for i in range(len(s)):
            # 奇數長度的回文（中心是 i）
            temp1 = expandAroundCenter(i, i)
            # 偶數長度的回文（中心是 i 和 i+1）
            temp2 = expandAroundCenter(i, i + 1)

            # 取較長者更新結果
            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2

        return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.cnt = 0
        self.result = ""

        def checkPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.cnt += 1
                if len(self.result) < (r - l + 1):
                    self.result = s[l : r + 1]

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
        return self.result
