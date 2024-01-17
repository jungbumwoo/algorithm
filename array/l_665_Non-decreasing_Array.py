from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/non-decreasing-array/

'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
'''

class Solution:
    def solve(self, nums: List[int]) -> bool:
        # Time Complexity : O(n) 
        # Space Complexity : O(1)
        if len(nums) <= 2:
            return True
        already = False
        at_least = nums[0]

        if nums[0] > nums[1]:
            already = True
            at_least = nums[1]

        for i in range(2, len(nums)):
            if nums[i] >= nums[i-1] and nums[i] >= at_least:
                continue
            elif nums[i] < nums[i-1]:
                if already is False:
                    already = True
                elif already is True:
                    return False
            elif nums[i] < at_least:
                if already is False:
                    already = True
                elif already is True:
                    return False
            else:
                at_least = nums[i]

        return True

'''
added condition, but failed to check initial status.
'''

        
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
                input=Args(nums = [4,2,3]),
                expect=True,
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [4,2,1]),
                expect=False
            ),
            TestCase(
                name="test 3",
                input=Args(nums = [3,4,2,3]),
                expect=False
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