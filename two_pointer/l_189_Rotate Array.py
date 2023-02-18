from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/rotate-array/

'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

class Solution:
    def solve(self, nums: List[int], k: int) -> None:
        length = len(nums)
        move = k % length
        
        if move == 0:
            return
        
        arr = nums[-move:] + nums[:-move]
        
        for i in range(len(arr)):
            nums[i] = arr[i]
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
                input=Args(nums = [1,2,3,4,5,6,7], k = 3),
                expect=[5,6,7,1,2,3,4]
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [-1,-100,3,99], k = 2),
                expect=[3,99,-1,-100]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(nums=c.input.nums, k=c.input.k)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
