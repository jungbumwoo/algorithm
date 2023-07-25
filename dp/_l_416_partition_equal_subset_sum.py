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

        calculated = [0]

        @functools.lru_cache(maxsize=None)
        def select(index: int, selected: bool):

            if calculated[0] == half:
                return True

            if index == len(nums):
                return False
            
            if selected:
                calculated[0] += nums[index]
                a = select(index + 1, True)
                calculated[0] -= nums[index]
                
                if a:
                    return True
                
                calculated[0] += nums[index]
                b = select(index + 1, False)
                calculated[0] -= nums[index]
                return True if b else False
            else:
                return select(index + 1, False) or select(index + 1, True)
        
        return select(0, True) or select(0, False)

        
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
