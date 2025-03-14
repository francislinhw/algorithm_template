# https://leetcode.com/problems/happy-number/description/


# 10 March 2025 practice
class Solution:
    def isHappy(self, n: int) -> bool:
        # 11.22

        # Step 1: Test happy number sum of square of its digit

        def sumOfSquareOfItsDigit(number: int) -> int:
            string = str(number)
            sumo = 0
            for num in string:
                sumo += int(num) ** 2
            return int(sumo)

        # Visited Set

        visited = set()

        happerTester = n

        while happerTester != 1:
            happerTester = sumOfSquareOfItsDigit(happerTester)
            print(happerTester)
            if happerTester not in visited:
                visited.add(happerTester)
            else:
                return False

        return True  # 11.30 8 min


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
