from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/maximum-subarray/description/

'''
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
'''

class Solution:
    def solve(self, nums: List[int]) -> int:
        # Time Complexity : O(n)
        # Space Complexity : O(n)
        data = [[0,0] for _ in range(len(nums))]
        
        data[0][0], data[0][1] = nums[0], nums[0]
        for i in range(1, len(nums)):
            data[i][0] = max(data[i-1][0], nums[i-1]) + nums[i]
            data[i][1] = max(data[i-1][0], data[i-1][1], nums[i-1])

        return max(data[-1][0], data[-1][1], nums[-1])

# 푼 기억이 없어서 풀었는데 더 잘풀었다.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        data = [0] * len(nums)
        data[0] = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            if data[i-1] <= 0:
                data[i] = nums[i]
            else:
                data[i] = data[i-1] + nums[i]
            
            ans = max(ans, data[i])
        
        return ans
                

        
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
                input=Args(nums = [-2,1,-3,4,-1,2,1,-5,4]),
                expect=6
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [5,4,-1,7,8]),
                expect=23
            ),
            TestCase(
                name="test 3",
                input=Args(nums = [1]),
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
