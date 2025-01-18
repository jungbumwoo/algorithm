class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price, max_price = 10 ** 4 + 1, 0
        profit = 0

        for i in range(len(prices)):
            price = prices[i]

            if price < min_price:
                min_price = price
            else:
                profit = max(price - min_price, profit)
        
        return profit
