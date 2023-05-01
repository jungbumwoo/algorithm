from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# Link

'''
description
'''

class Solution:
    def solve(self, target: int, nums: List[int]) -> int:
        # Time Complexity : O(n)
        # Space Complexity :  O(1)
        l, r, total = 0, 1, nums[0]
        ans = 10 ** 6
        while r <= len(nums):
            if total < target:
                if r < len(nums):
                    total += nums[r]
                r += 1
            else:
                ans = min(r - l, ans)
                total -= nums[l]
                l += 1

        if ans == 10 ** 6:
            return 0
        return ans


        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            target: int
            nums: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(target = 7, nums = [2,3,1,2,4,3]),
                expect=2
            ),
            TestCase(
                name="test 2",
                input=Args(target = 4, nums = [1,4,4]),
                expect=1
            ),
            TestCase(
                name="test 3",
                input=Args(target = 11, nums = [1,1,1,1,1,1,1,1]),
                expect=0
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(target=c.input.target, nums=c.input.nums)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()

