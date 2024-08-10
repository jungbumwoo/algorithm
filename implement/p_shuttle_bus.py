from dataclasses import dataclass
from typing import List
import unittest


# https://school.programmers.co.kr/learn/courses/30/lessons/17678

'''
description
'''

class Solution:
    def solution(self, n, t, m, timetable):
        arr = []
        
        max_arrive = 9 * 60 + int(n) * int(t)
        
        for time in timetable:
            h, m = time.split(":")
            if int(h) * 60 + int(m) <= max_arrive:
                arr.append(int(h) * 60 + int(m))

        sorted(arr)
        arrive = 9 * 60
        index = self.get_index(n, m, t, arrive, arr)
        
        if index == len(arr) - 1:
            should = arr[index] - 1
        else:
            should = max_arrive
        
        if should >= 24 * 60:
            return "23:59"    
        
        h = should // 60
        if h < 10:
            h = '0' + str(h)
        else:
            h = str(h)
        m = should % 60
        if m < 10:
            m = '0' + str(m)
        else:
            m = str(m)
        return h + ':' + m
    
        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            n: int
            t: int
            m: int
            timetable: List[str]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            # TestCase(
            #     name="test 1",
            #     input=Args(n=1, t=1, m=5, timetable=["08:00", "08:01", "08:02", "08:03"]),
            #     expect="09:00"
            # ),
            TestCase(
                name="test 2",
                input=Args(n=2, t=10, m=2, timetable=["09:10", "09:09", "08:00"]),
                expect="09:09"
            ),
            TestCase(
                name="test 3",
                input=Args(n=2, t=1, m=2, timetable=["09:00", "09:00", "09:00", "09:00"]),
                expect="08:59"
            ),
            TestCase(
                name="test 4",
                input=Args(n=1, t=1, m=5, timetable=["00:01", "00:01", "00:01", "00:01", "00:01"]),
                expect="00:00"
            ),
            TestCase(
                name="test 5",
                input=Args(n=1, t=1, m=1, timetable=["23:59"]),
                expect="09:00"
            ),
            TestCase(
                name="test 6",
                input=Args(n=10, t=60, m=45, timetable=["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]),
                expect="18:00"
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solution(n=c.input.n, t=c.input.t, m=c.input.m, timetable=c.input.timetable)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
