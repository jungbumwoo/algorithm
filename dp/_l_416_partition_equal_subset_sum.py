from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest
import functools

# https://leetcode.com/problems/partition-equal-subset-sum/

'''
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such 
that the sum of the elements in both subsets is equal or false otherwise.
'''

class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        # Time Complexity :  
        # Space Complexity : 
        total = sum(nums)
        isFalse = total % 2

        if isFalse:
            return False

        half = total // 2

        @functools.lru_cache(maxsize=None)
        def select(index: int, selected: bool, calculated: int):

            if calculated == half:
                return True

            if index == len(nums):
                return False
            
            if selected:
                calculated += nums[index]
                a = select(index + 1, True, calculated)
                calculated -= nums[index]
                
                if a is True:
                    return True
                
                calculated += nums[index]
                b = select(index + 1, False, calculated)
                calculated -= nums[index]
                return True if b is True else False
            else:
                return select(index + 1, False, calculated) or select(index + 1, True, calculated)
        
        return select(0, True, 0) or select(0, False, 0)

        
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
            expect: bool

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums = [1,5,11,5]),
                expect=True,
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [1,2,3,5]),
                expect=False,
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
