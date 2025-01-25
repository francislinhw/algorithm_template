# https://leetcode.com/problems/happy-number/description/


class Solution:
    def isHappy(self, n: int) -> bool:
        duplicate = set()
        while True:
            rut = 0
            numberString = str(n)
            for num in numberString:
                rut += int(num) ** 2

            if rut in duplicate:
                return False
            duplicate.add(rut)

            if rut == 1:
                return True
            n = rut
        # not recomend recurrsive
