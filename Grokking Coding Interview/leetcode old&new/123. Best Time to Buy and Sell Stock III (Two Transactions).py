class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        def profit(start, end):
            least = float("inf")
            max_profit = 0

            for x in range(start, end):
                curr = prices[x]

                least = min(curr, least)
                diff = curr - least

                max_profit = max(max_profit, diff)

            return max_profit

        tmp_max = 0

        for x in range(0, len(prices)):
            n = len(prices)

            tmp_val = profit(0, x) + profit(x, n)
            tmp_max = max(tmp_max, tmp_val)

        return tmp_max


