from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/maximum-average-subarray-i/

'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start, end = 0, k
        window_value = sum(nums[start:end])
        max_value = window_value

        while True:
            window_value -= nums[start]
            start += 1
            end += 1

            if end > len(nums):
                break

            window_value += nums[end-1]
            if max_value < window_value:
                max_value = max(window_value, max_value)

        return max_value / k            

        
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
                input=Args(nums = [1,12,-5,-6,50,3], k=4),
                expect=12.75000
            ),
            # TestCase(
            #     name="test 2",
            #     input=Args(nums = [5], k=1),
            #     expect=5.00000
            # ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.findMaxAverage(nums=c.input.nums, k=c.input.k)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
