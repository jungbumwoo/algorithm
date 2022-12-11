from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/valid-triangle-number/

'''
description
'''

class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        # Time Complexity :  
        # Space Complexity : 
        # [2,2,3,4]
        picked = set()

        def find(index, left, right):
            print('----------------------------------------------------------------')
            if left >= right:
                return 0
            
            ans = 0
            while left < right:
                print('while', left, right, nums[left], nums[right])
                if nums[left] == 0:
                    left += 1
                    continue
                
                if nums[left] + nums[index] > nums[right]:
                    if (index, left, right) not in picked:
                        ans += 1
                        left += 1
                        picked.add((index, left, right))
                elif nums[left] + nums[index] == nums[right]:
                    ans += find(index, left + 1, right)
                    ans += find(index, left, right - 1)
                else:
                    right -= 1
            print(nums[index], left, right, ans)
            return ans
        
        if len(nums) < 3:
            return 0
        
        nums.sort()
        result = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                continue
            result += find(i, i+1, len(nums)-1)
        return result

        
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
                input=Args(nums = [2,2,3,4]),
                expect=3
            ),
            # TestCase(
            #     name="test 2",
            #     input=Args(nums = [4,2,3,4]),
            #     expect=4
            # ),
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
