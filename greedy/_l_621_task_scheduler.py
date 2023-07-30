from dataclasses import dataclass
from typing import List, Optional, Tuple

import heapq
import unittest
import collections


#  https://leetcode.com/problems/task-scheduler/

'''
description
'''

class Solution:
    def solve(self, tasks: List[str], n: int) -> int:
        # Time Complexity :  
        # Space Complexity : 
        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            tasks: List[int]
            n: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(tasks = ["A","A","A","B","B","B"], n=2),
                expect=8
            ),
            TestCase(
                name="test 2",
                input=Args(tasks = ["A","A","A","B","B","B"], n=0),
                expect=6
            ),
            TestCase(
                name="test 3",
                input=Args(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n=2),
                expect=16
            ),
            TestCase(
                name="test 4",
                input=Args(tasks = ["A","A","A","B","B","B","C","C","C"], n=2),
                expect=9
            ),
            TestCase(
                name="test 5",
                input=Args(tasks = ["A","B","C","D","E"], n=0),
                expect=5
            ),
            TestCase(
                name="test 6",
                input=Args(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n=0),
                expect=12
            ),
            TestCase(
                name="test 7",
                input=Args(tasks = ["A","A","A","A","A","A","B","B","B","B","B","B","C","C","C","C","C","C","D","D"], n=2),
                expect=20
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(tasks=c.input.tasks, n=c.input.n)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()


import heapq

class Solution:
    def solve(self, tasks: List[str], n: int) -> int:
        # 1
        raw = {}
        for i in range(len(tasks)):
            if tasks[i] in raw:
                raw[tasks[i]] += 1
            else:
                raw[tasks[i]] = 1

        queue = []
        heapq.heapify(queue)        

        for k, v in raw.items():
            heapq.heappush(queue, [v, k])

        empty = 0
        cnt = 0
        while queue:
            temp = []
            empty = 0
            for _ in range(n+1):
                cnt += 1
                try:
                    v, k = queue.heappop()

                    v -= 1

                    if v:
                        temp.append([v, k])
                except:
                    empty += 1
                    continue

            for q in range(len(temp)):
                heapq.heappush(queue, [temp[q][0], temp[q][1]])

        return cnt - empty