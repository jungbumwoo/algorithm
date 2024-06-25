'''
fixme:

memory exceeded
'''

from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        return self.select(0, 0, False, 0)

    @lru_cache(None)
    def select(self, index, count, is_hold, cost):
        if index >= len(self.prices):
            return 0
        
        if count >= 2:
            return 0

        ans = 0
        if is_hold:
            sell = self.select(index+1, count+1, False, 0) + self.prices[index] - cost
            not_sell = self.select(index+1, count, is_hold, cost)
            ans = max(ans, sell, not_sell)
        else:
            buy = self.select(index+1, count, True, self.prices[index])
            not_buy = self.select(index+1, count, is_hold, cost)
            ans = max(ans, buy, not_buy)
        
        return ans