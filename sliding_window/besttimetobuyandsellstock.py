# Question: Given prices array, return the maximum profit. You must buy before you sell.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for cost in prices:
            if cost < min_price:
                min_price = cost

            if (cost - min_price) > max_profit:
                max_profit = cost - min_price

        return max_profit
