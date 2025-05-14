# https://leetcode.com/problems/multiply-strings/description/
class Solution(object):
    def multiply(self, num1, num2):
        # 1.10
        if num1 == "0" or num2 == "0":
            return "0"

        # 預先開好結果位數：最多 len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))

        # 反轉方便從個位數開始乘
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = int(num1[i]) * int(num2[j])
                res[i + j] += mul
                # 處理進位
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        # 去掉前導 0
        while res[-1] == 0:
            res.pop()

        return "".join(map(str, res[::-1]))


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                digits = int(num1[i]) * int(num2[j])
                res[i + j] += digits
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        res = res[::-1]
        ptr = 0
        while res[ptr] == 0:
            ptr += 1

        res = res[ptr:]
        for i in range(len(res)):
            res[i] = str(res[i])
        return "".join(res)
