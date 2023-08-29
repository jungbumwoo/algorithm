from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# fixme: failed casee exists.
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

'''
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
'''

class Solution:
    def solve(self, weights: List[int], days: int) -> List[int]:

        # Time Complexity :  N * log M, N: len(weights) M: sum(weights)
        # Space Complexity : O(1)

        if len(weights) == 1:
            return 1

        left, right = min(weights), sum(weights)
        ans = 0

        while left <= right:
            m = (left + right) // 2

            cnt = 1
            temp = 0
            print(left, right, m)
            for i in range(len(weights)):
                if temp + weights[i] <= m:
                    temp += weights[i]
                elif weights[i] > m:
                    cnt = 5 * (10 ** 4) + 1
                    break
                else:
                    temp = weights[i]
                    cnt += 1

            if cnt > days:
                left = m + 1
            else:
                right = m - 1
                ans = m
        
        return ans

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            weights: List[int]
            days: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(weights = [1,2,3,4,5,6,7,8,9,10], days = 5),
                expect=15
            ),
            TestCase(
                name="test 2",
                input=Args(weights = [3,2,2,4,1,4], days = 3),
                expect=6
            ),
            TestCase(
                name="test 3",
                input=Args(weights = [1,2,3,1,1], days = 4),
                expect=3
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(weights=c.input.weights, days=c.input.days)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
