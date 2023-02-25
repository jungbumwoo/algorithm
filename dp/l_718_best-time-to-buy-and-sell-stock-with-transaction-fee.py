from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''


class Solution:
    def solve(self, prices: List[int], fee: int) -> int:
        @lru_cache(maxsize=None)
        def pick(i, was_buy):
            if i == len(prices):
                return 0
            
            if was_buy:
                a = pick(i + 1, False) + prices[i]
                b = pick(i + 1, was_buy)
            else:
                a = pick(i + 1, True) - prices[i] - fee
                b = pick(i + 1, was_buy)
            ans = max(a, b)
            return ans

        return pick(0, False)
    
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            prices: List[int]
            fee: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(prices = [1,3,2,8,4,9], fee = 2),
                expect=8
            ),
            TestCase(
                name="test 2",
                input=Args(prices = [1,3,7,5,10,3], fee = 3),
                expect=6
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(prices=c.input.prices, fee=c.input.fee)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()


