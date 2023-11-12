from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/boats-to-save-people/description/

'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
'''

class Solution:
    def solve(self, people: List[int], limit: int) -> int:
        # Time Complexity :  O(n)
        # Space Complexity : O(n)

        if len(people) == 1:
            return 1

        people.sort()
        left, right = 0, len(people) - 1
        boarded = [False] * len(people)
        count = 0
        
        while left <= right:

            boat = limit
            maxi = 2

            while boat >= people[right] and boarded[right] is False and maxi > 0:
                boat -= people[right]
                boarded[right] = True
                right -= 1
                maxi -= 1
            
            while boat >= people[left] and boarded[left] is False and maxi > 0:
                boat -= people[left]
                boarded[left] = True
                left += 1
                maxi -= 1
            
            count += 1

        return count
        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            people: List[int]
            limit: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(people = [1,2], limit = 3),
                expect=1
            ),
            TestCase(
                name="test 2",
                input=Args(people = [3,2,2,1], limit = 3),
                expect=3
            ),
            TestCase(
                name="test 3",
                input=Args(people = [3,5,3,4], limit = 5),
                expect=4
            ),
            TestCase(
                name="test 4",
                input=Args(people = [3,2,3,2,2], limit = 6),
                expect=3
            )
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(people=c.input.people, limit=c.input.limit)
            print(c.name, '✅')
            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
