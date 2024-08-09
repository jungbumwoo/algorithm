from dataclasses import dataclass
from typing import List
import unittest


# https://school.programmers.co.kr/learn/courses/30/lessons/67258

'''
description
'''
class Pocket:
    def __init__(self, num_max_kind):
        self.bucket = {}
        self.num_max_kind = num_max_kind
    
    def put(self, jem: str):
        if jem in self.bucket:
            self.bucket[jem] += 1
        else:
            self.bucket[jem] = 1
    
    def out(self, jem: str):
        if jem not in self.bucket:
            raise ValueError('unexpected')
        
        if self.bucket[jem] == 1:
            del self.bucket[jem]
        else:
            self.bucket[jem] -= 1
    def is_full(self):
        return len(self.bucket) == self.num_max_kind


class Solution:
    def solution(self, gems):
        if len(gems) == 1:
            return [1,1]
        
        ans = [1, 1000001]
        left, right = 0, -1
        pocket = Pocket(num_max_kind=len(set(gems)))
        
        while right < len(gems):
            while right + 1 < len(gems):
                right += 1
                pocket.put(gems[right])
                
                if pocket.is_full() is True:
                    if ans[1] - ans[0] > right - left:
                        ans[0], ans[1] = left, right
                    break
                
            
            while left < right:
                pocket.out(gems[left])
                left += 1
                if pocket.is_full() is True:
                    if ans[1] - ans[0] > right - left:
                        ans[0], ans[1] = left, right
                else:
                    break

            if left > right:
                break
            if left == len(gems) - 1 and right == len(gems) - 1:
                break

        return [ans[0] + 1, ans[1] + 1]


        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            gems: List[str]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]),
                expect=[3, 7]
            ),
            TestCase(
                name="test 2",
                input=Args(gems=["AA", "AB", "AC", "AA", "AC"]),
                expect=[1, 3]
            ),
            TestCase(
                name="test 2",
                input=Args(gems=["XYZ", "XYZ", "XYZ"]),
                expect=[1, 1]
            ),
            TestCase(
                name="test 2",
                input=Args(gems=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]),
                expect=[1, 5]
            ),
        ]

        solution = Solution()
        for c in cases:
            print(f'c.input.gems: {c.input.gems}')
            actual = solution.solution(gems=c.input.gems)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
