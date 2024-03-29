from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# Link

'''
description
'''

class Solution:
    def solve(self, n: int, primes: List[int]) -> int:

        dp = [0] * n
        dp[0] = 1
        min_values = primes[:]

        for i in range(1, len(dp)):
            new = min(min_values)
            index = min_values.index(new)

            dp[i] = new
            min_values[index] = min_values[index] * primes[index]
        
        print(min_values)
        print(dp)
        return dp[-1]
        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            nums: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums = [-4,-1,0,3,10]),
                expect=[0,1,9,16,100]
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [-7,-3,2,3,11]),
                expect=[4,9,9,49,121]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(nums=c.input.nums)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
