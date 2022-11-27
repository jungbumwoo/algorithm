from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# Link

'''
Given an integer array nums,
Find one continuous subarray that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.
'''

class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        # Time Complexity :  
        # Space Complexity : 
        if len(nums) <2:
            return 0

        prev = nums[0]
        end = 0
		# find the largest index not in place
        for i in range(0, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        start = len(nums) - 1
        prev = nums[start]
		# find the smallest index not in place
        for i in range(len(nums)-1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        if end != 0:
            return end - start + 1
        else: 
            return 0

        
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
                name="test 0",
                input=Args(nums = [1, 3, 5, 4, 2]),
                expect=4
            ),
            TestCase(
                name="test 1",
                input=Args(nums = [2,6,4,8,10,9,15]),
                expect=5
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [1,2,3,4]),
                expect=0
            ),
            TestCase(
                name="test 3",
                input=Args(nums = [1]),
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

