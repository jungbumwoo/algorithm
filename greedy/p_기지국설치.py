from dataclasses import dataclass
from typing import List
import unittest


# https://school.programmers.co.kr/learn/courses/30/lessons/12979

'''
description
'''

class Solution:
    def solve(self, n, stations, w):
        if len(stations) == 0:
            if n % ((2 * w) + 1) == 0:
                return n // ((2 * w) + 1)
            else:
                return n // ((2 * w) + 1) + 1
        
        k = 1
        index = 0
        answer = 0
        while k <= n:
            print(f'n: {n}, k: {k}, index: {index}, answer: {answer}')
            if index < len(stations):
                left, right = stations[index] - w, stations[index] + w

                if k >= left:
                    k = right + 1
                    index += 1
                else:
                    k += 2 * w + 1
                    answer += 1
            else:
                k += 2 * w + 1
                answer += 1
        
        return answer


        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            n: int
            stations: List[int]
            w: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(n=11, stations=[4, 11], w=1),
                expect=3
            ),
            TestCase(
                name="test 2",
                input=Args(n=16, stations=[9], w=2),
                expect=3
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(n=c.input.n, stations=c.input.stations, w=c.input.w)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
