import sys
import io


class Solution:
    def max_profit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0, 0
        transactions = []

        i = 0
        while i < n - 1:
            while i < n - 1 and prices[i] > prices[i + 1]:
                i += 1
            if i == n - 1:
                break
            buy = i
            i += 1

            while i < n and prices[i] >= prices[i - 1]:
                i += 1
            sell = i - 1

            transactions.append((buy, sell))

        transactions.sort(
            key=lambda x: (-(prices[x[1]] - prices[x[0]]), x[1] - x[0], x[0])
        )

        selected_transactions = []
        total_profit = 0

        for buy, sell in transactions:
            if len(selected_transactions) < k:
                if total_profit + prices[sell] - prices[buy] > total_profit:
                    selected_transactions.append((buy, sell))
                    total_profit += prices[sell] - prices[buy]
                elif len(selected_transactions) == k:
                    break

        return total_profit, len(selected_transactions)

    def main(self):
        for line in sys.stdin:
            data = line.strip().split(";")
            numbers = list(map(int, data[0].split(",")))
            target = int(data[1])

            x, y = self.max_profit(numbers, target)
            print(f"{x},{y}")
            return f"{x},{y}"

    def test_max_profit(self):
        # Test the function with io.StringIO
        sys.stdin = io.StringIO("1,2,3,2,1,1,2,4,8,2,2;3")
        res = self.main()
        assert res == "9,2"

        sys.stdin = io.StringIO("1,2,3,2,1,1,2,4,8,2,2,4,5;3")
        res = self.main()
        assert res == "12,3"

        sys.stdin = io.StringIO("1,2,3,4,1,2,3,4;3")
        res = self.main()
        assert res == "6,2"

        sys.stdin = io.StringIO("1,2,3,4,1,2,3,4;10")
        res = self.main()
        assert res == "6,2"


if __name__ == "__main__":
    solution = Solution()
    solution.test_max_profit()
