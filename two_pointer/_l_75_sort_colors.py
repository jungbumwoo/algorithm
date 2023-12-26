from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/sort-colors/description/

'''
더 개선해 볼 것. 더 잘 풀 수 있음.
'''

class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        # Time Complexity :  O(N)
        # Space Complexity : O(1)
        self.arrange(0, 2, nums)
        self.arrange(1, 2, nums)
        self.arrange(0, 1, nums)
        return nums

    def arrange(self, left, right, nums: List[int]) -> None:
        if len(nums) == 0:
            return
        
        l_index, r_index = 0, len(nums) - 1

        while l_index < r_index:

            if nums[l_index] == right:
                if nums[r_index] == left:
                    nums[l_index], nums[r_index] = left, right
                    l_index += 1
                    r_index -= 1
                else:
                    r_index -= 1
            elif nums[r_index] == left:
                l_index += 1
            else:
                l_index += 1
                r_index -= 1


        
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
                input=Args(nums = [2,0,2,1,1,0]),
                expect=[0,0,1,1,2,2]
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [2,0,1]),
                expect=[0,1,2]
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

