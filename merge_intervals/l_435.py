import heapq
from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/non-overlapping-intervals

'''
description
'''

class Solution:


    def solve1(self, intervals: List[List[int]]) -> int:
        cache = []
        heapq.heapify(cache)
        answer = 0
        intervals.sort(key=lambda x:x[1] - x[0])
        print(len(intervals))
        print(intervals)

        for interval in intervals:
            s, e = interval

            flag = True
            for cached in cache:
                cached_start, cached_end = cached[0], cached[1]

                if (cached_start < e and cached_end > s) or (cached_end > s and cached_start < e):
                    answer += 1
                    print('already', cache, cached_start, cached_end, s, e, answer)
                    flag = False
                    break
            
            if flag:
                print('cached', [s, e])
                heapq.heappush(cache, [s, e])
        return answer

    def solve2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], x[1]))
        answer = 0
        last_point = -(10**5)
        for interval in intervals:
            start, end = interval[0], interval[1]

            if start < last_point:
                last_point = min(last_point, end) # 여기서 이게 빠지면 안됨
                answer += 1
            else:
                last_point = end
        
        return answer

    def solve3(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        answer = 0
        last_point = -(10**5)
        for interval in intervals:
            start, end = interval[0], interval[1]

            if start < last_point:
                last_point = min(last_point, end)
                answer += 1
            else:
                last_point = end
        
        return answer


        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            intervals: List[List[int]]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(intervals = [[1,2],[2,3],[3,4],[1,3]]),
                expect=1
            ),
            TestCase(
                name="test 2",
                input=Args(intervals = [[1,2],[1,2],[1,2]]),
                expect=2
            ),
            TestCase(
                name="test 3",
                input=Args(intervals = [[1,2],[2,3]]),
                expect=0
            ),
            TestCase(
                name="test 4",
                input=Args(intervals = [[-25322,-4602],[-35630,-28832],[-33802,29009],[13393,24550],[-10655,16361],[-2835,10053],[-2290,17156],[1236,14847],[-45022,-1296],[-34574,-1993],[-14129,15626],[3010,14502],[42403,45946],[-22117,13380],[7337,33635],[-38153,27794],[47640,49108],[40578,46264],[-38497,-13790],[-7530,4977],[-29009,43543],[-49069,32526],[21409,43622],[-28569,16493],[-28301,34058]]),
                expect=19
            ),
            TestCase(
                name="test 5",
                input=Args(intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]),
                expect=7
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve2(intervals=c.input.intervals)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
