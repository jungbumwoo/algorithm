from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/longest-consecutive-sequence/description/

'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        # Time Complexity : O(n)
        # Space Complexity : O(n)
        data = dict()
        ans = 1

        for i in range(len(nums)):

            num = nums[i]
            big = nums[i] + 1
            small = nums[i] - 1

            if small == -1:
                small = 0

            if num not in data:
                if big in data and small in data:
                    data[data[small][0]][1] = data[big][1]
                    data[data[big][1]][0] = data[small][0]
                    ans = max(data[big][1] - data[small][0] + 1, ans)

                    data[num] = [data[small][0], data[big][1]]
                elif big in data:
                    data[big][0] = num
                    data[num] = [num, data[big][1]]
                    ans = max(data[big][1] - num + 1, ans)
                elif small in data:
                    data[small][1] = num
                    data[num] = [data[small][0], num]
                    ans = max(num - data[small][0] + 1, ans)
                else:  # (if, continue) is hard to debug. so change to if, elif, else
                    data[num] = [num, num] # min, max
        
        return ans


'''
comment: when update window, find the correct point that need to be updated
'''

        
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
                input=Args(nums = [100,4,200,1,3,2]),
                expect=4
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [0,3,7,2,5,8,4,6,0,1]),
                expect=9
            ),
            TestCase(
                name="test 3",
                input=Args(nums = [100,4,200,1,3,2,6,7,8,10,11,9,5]),
                expect=11
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
