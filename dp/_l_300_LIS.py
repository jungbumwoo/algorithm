import unittest

from dataclasses import dataclass
from functools import lru_cache
from typing import List, Optional, Tuple



# https://leetcode.com/problems/longest-increasing-subsequence/description/

'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
'''

class Solution:
    # Memory Limit Exceeded
    def solve(self, nums: List[int]) -> bool:
        constraint_min = - (10 ** 4) - 1
        @lru_cache(maxsize=None)
        def select(i, before_picked):

            if i == len(nums):
                return 0

            current = nums[i]
            picked = constraint_min
            if current > before_picked:
                # picked
                picked = select(i+1, current) + 1

            # not picked
            not_picked = select(i+1, before_picked)

            return max(picked, not_picked)
        return select(0, constraint_min)

        
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
                input=Args(nums = [10,9,2,5,3,7,101,18]),
                expect=4,
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [0,1,0,3,2,3]),
                expect=4,
            ),
            TestCase(
                name="test 3",
                input=Args(nums = [7,7,7,7,7,7,7]),
                expect=1
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