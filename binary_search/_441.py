from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/arranging-coins

'''

'''

class Solution:
    def solve(self, n: int) -> int:
        # Time Complexity :  O(log(n))
        # Space Complexity : O(1)
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2

            k = mid * (mid + 1) // 2
            if k == n:
                return mid

            if k > n:
                right = mid - 1
            elif k < n:
                left = mid + 1

        return right

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            n: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(n=5),
                expect=2
            ),
            TestCase(
                name="test 2",
                input=Args(n=8),
                expect=3
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(n=c.input.n)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
