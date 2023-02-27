# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

'''
You are given an integer array prices where prices[i] is 
the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 

You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, canBuy):
            if i == len(prices):
                return 0
            
            if canBuy:
                a = dp(i+1, False) - prices[i]  # Buy
                b = dp(i+1, canBuy)  # Skip
            else:
                a = dp(i+1, True) + prices[i]  # Sell
                b = dp(i+1, canBuy)  # Skip
            ans = max(a, b)
            return ans
        
        return dp(0, True)