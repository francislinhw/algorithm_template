# https://leetcode.com/problems/integer-to-roman/


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
            M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]
        )


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit = [0 for _ in range(4)]  # 千、百、十、個

        digit[0] = num // 1000
        digit[1] = (num % 1000) // 100
        digit[2] = (num % 100) // 10
        digit[3] = num % 10

        res = ""

        # 千位
        th = digit[0]
        res += "M" * th

        # 百位
        hr = digit[1]
        if hr <= 3:
            res += "C" * hr
        elif hr == 4:
            res += "CD"
        elif hr == 5:
            res += "D"
        elif hr <= 8:
            res += "D" + "C" * (hr - 5)
        elif hr == 9:
            res += "CM"

        # 十位
        ten = digit[2]
        if ten <= 3:
            res += "X" * ten
        elif ten == 4:
            res += "XL"
        elif ten == 5:
            res += "L"
        elif ten <= 8:
            res += "L" + "X" * (ten - 5)
        elif ten == 9:
            res += "XC"

        # 個位
        ind = digit[3]
        if ind <= 3:
            res += "I" * ind
        elif ind == 4:
            res += "IV"
        elif ind == 5:
            res += "V"
        elif ind <= 8:
            res += "V" + "I" * (ind - 5)
        elif ind == 9:
            res += "IX"

        return res
