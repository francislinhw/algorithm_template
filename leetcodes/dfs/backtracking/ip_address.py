# https://leetcode.com/problems/restore-ip-addresses/description/

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(sub):
            # 不可以為空，不能有前導 0（除非是單個 '0'），必須是 0~255 的數字
            if not sub:
                return False
            if len(sub) > 1 and sub[0] == "0":
                return False
            return 0 <= int(sub) <= 255

        res = []

        def dfs(index, address, pointsLeft):
            if pointsLeft == 0:
                last = s[index:]
                if isValid(last):
                    fullAddress = address + [last]
                    res.append(".".join(fullAddress))
                return

            for i in range(1, 4):  # 每段長度為 1～3
                if index + i > len(s):
                    break
                part = s[index : index + i]
                if isValid(part):
                    address.append(part)
                    dfs(index + i, address, pointsLeft - 1)
                    address.pop()

        dfs(0, [], 3)
        return res


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def isValid(part):
            # 要求：不超過 255，不能有前導 0（除非是 '0'）
            if not part:
                return False
            if len(part) > 1 and part[0] == "0":
                return False
            return 0 <= int(part) <= 255

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):  # 長度 1～3
                part = s[start:end]
                if isValid(part):
                    backtrack(end, path + [part])

        backtrack(0, [])
        return res
