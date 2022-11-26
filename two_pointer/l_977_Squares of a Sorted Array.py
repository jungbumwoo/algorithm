from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/squares-of-a-sorted-array/

'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares_two_sum(self, nums: List[int]) -> List[int]:
        # Time Complexity : O(n) 
        # Space Complexity : O(n)
        arr = [None] * len(nums)

        index = len(nums) - 1
        left, right = 0, len(nums) - 1

        while left <= right:
            l_square, r_square = nums[left] * nums[left], nums[right] * nums[right]
            
            if l_square > r_square:
                arr[index] = l_square
                index -= 1
                left += 1
            else:
                arr[index] = r_square
                index -= 1
                right -= 1

        return arr


    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time Complexity : O(n * logn) 
        # Space Complexity : O(n)

        arr = []
        if nums[0] >= 0:
            for i in range(len(nums)):
                arr.append(nums[i] * nums[i])
            return arr
            
        if nums[-1] <= 0:
            for i in range(len(nums)-1, -1, -1):
                arr.append(nums[i] * nums[i])
            return arr
        
        for i in range(len(nums)):
            arr.append(nums[i] * nums[i])
        
        return sorted(arr)
        
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
            actual = solution.sortedSquares_two_sum(nums=c.input.nums)
            # actual = solution.sortedSquares(nums=c.input.nums)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()