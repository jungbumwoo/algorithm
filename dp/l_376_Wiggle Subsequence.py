from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/wiggle-subsequence/

'''
2번 다르게 틀림.
'''

class Solution:
    def solve(self, nums: List[int]) -> int:
        # Time Complexity :  
        # Space Complexity : 
        if len(nums) == 0:
            return 0
        
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def search(index, before, is_up):

            if index == len(nums):
                return 0

            diff = nums[index] - before
            a, b, c, d, e = 0, 0, 0, 0, 0
            if diff > 0 and is_up is False:
                a = search(index + 1, nums[index], True) + 1
            elif diff > 0 and is_up is True:
                b = search(index + 1, before, True)
            elif diff < 0 and is_up is True:
                c = search(index + 1, nums[index], False) + 1
            elif diff < 0 and is_up is False:
                d = search(index + 1, before, False)
            else:
                # raise Error
                e = search(index + 1, before, is_up)
            
            return max(a, b, c, d, e)
        
        return max(search(0, nums[0] - 1, False), search(0, nums[0] + 1, True)) 
        

        
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
                input=Args(nums = [1,7,4,9,2,5]),
                expect=6
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [1,2,3,4,5,6,7,8,9]),
                expect=2
            ),
            TestCase(
                name="test 3",
                input=Args(nums = [1,2,3]),
                expect=2
            ),
            # TestCase(
            #     name="test 4",
            #     input=Args(nums = [33,53,12,64,50,41,45,21]),
            #     expect=7
            # ),
            TestCase(
                name="test 5",
                input=Args(nums = [64,50,41,45,21]),
                expect=4
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = sol
            ution.solve(nums=c.input.nums)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
