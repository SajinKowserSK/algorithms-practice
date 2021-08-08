import sys

class Solution(object):
    def maxProfit(self, prices):

        max_val = 0
        min_val = sys.maxsize
        for x in range(0, len(prices)):
            if prices[x] < min_val:
                min_val = prices[x]

            else:
                diff = prices[x] - min_val
                max_val = max(max_val, diff)

        return max_val
