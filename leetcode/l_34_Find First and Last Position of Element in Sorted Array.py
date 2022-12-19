from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

'''
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def solve(self, nums: List[int], target: int) -> List[int]:
        # print(nums)
        def find_min(left, right, target):
            if left < 0 or right >= len(nums):
                return -1

            while left <= right:
                mid = (left + right) // 2
                # print(f'left: {left}, nums[left]: {nums[left]}, right: {right}, nums[right]: {nums[right]}, mid: {mid}, nums[mid]:{nums[mid]}')
                if nums[mid] < target:  
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    if mid == 0 or nums[mid-1] != target:
                        return mid
                    else:
                        right = mid - 1
            
            return -1

        def find_max(left, right, target):
            if left < 0 or right >= len(nums):
                return -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1       
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    if mid == len(nums) -1 or nums[mid+1] != target:
                        return mid
                    else:
                        left = mid + 1

            return -1

        if len(nums) == 0:
            return [-1, -1]

        l = find_min(0, len(nums) -1, target)
        r = find_max(0, len(nums) -1, target)
        return [l, r]
        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            nums: List[int]
            target: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums = [5,7,7,8,8,10], target = 8),
                expect=[3,4]
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [5,7,7,8,8,10], target = 6),
                expect=[-1,-1]
            ),
            TestCase(
                name="test 3",
                input=Args(nums = [], target = 0),
                expect=[-1,-1]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(nums=c.input.nums, target=c.input.target)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()

