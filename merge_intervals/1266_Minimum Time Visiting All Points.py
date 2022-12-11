from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# Link

'''
description
'''

class Solution:
    def solve(self, points: List[int]) -> int:
        # Time Complexity :  
        # Space Complexity : 
        raise NotImplementedError

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            points: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(points = [[1,1],[3,4],[-1,0]]),
                expect=7
            ),
            TestCase(
                name="test 2",
                input=Args(points = [[3,2],[-2,2]]),
                expect=5
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(points=c.input.points)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
