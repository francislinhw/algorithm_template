# https://leetcode.com/problems/count-and-say/description/


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        def encoding(string):
            string += "%"  # illegal
            res = ""
            cnt = 1
            prev = string[0]
            for i in range(1, len(string)):
                word = string[i]
                if prev == word:
                    cnt += 1
                else:
                    res += str(cnt) + prev
                    cnt = 1
                prev = word
            return res

        result = "1"
        for _ in range(n - 1):  # 注意是 n-1 次
            result = encoding(result)

        return result


import itertools


class Solution(object):
    def countAndSay(self, n):
        res = "1"
        for _ in range(n - 1):
            res = "".join(
                str(len(list(group))) + digit for digit, group in itertools.groupby(res)
            )
        return res
