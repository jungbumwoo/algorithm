from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/maximum-gap

'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space
'''

class Solution:
    def solve(self, nums: List[int]) -> None:
        return
            

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            nums: List[int]
            k: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums = [3,6,9,1]),
                expect=3
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [10]),
                expect=0
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
