class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        cache = {}

        pick(0, 'sell-pass') 

        def pick(i, was_buy):
            if i >= len(prices):
                return 0
            if (i, was_buy) in cache:
                return cache[(i, was_buy)]
            
            if was_buy == 'buy':
                a = pick(i + 1, 'sell') + prices[i]
                b = pick(i + 1, 'buy-pass')
            elif was_buy == 'sell':
                a = pick(i + 1, 'sell-pass')
                b = 0 
            elif was_buy == 'sell-pass':
                a = pick(i + 1, 'buy') - prices[i]
                b = pick(i + 1, 'sell-pass')
            elif was_buy == 'buy-pass':
                a = pick(i + 1, 'buy-pass')
                b = pick(i + 1, 'sell') + prices[i]
            
            ans = max(a, b)

            cache[(i, was_buy)] = ans
            return ans

            
        return pick(0, 'sell-pass')