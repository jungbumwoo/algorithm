from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# Link

'''
저축한 날짜에서 마지막 저축한 날짜까지 매일 저축하였으면 '1일1저축'에 성공!
첫 저축을 시작한 문자열 s, 다음 저축 까지 걸린 기간을 담은 문자열 배열 times가 주어짐.
'1일1저축' 성공 여부, 저축 기간(일)을 배열에 담아 return 하시오.

* 제한 *
윤년 없음. 모든 달은 30일. 1년 360일이라고 가정함
s: YYYY:MM:DD:HH:mm:ss 형태의 문자열
times의 element : DD:MM:mm:SS 형태의 문자열

0 <= times 의 길이 <= 1,000

1 <= DD <= 30
0 <= HH <= 23
0 <= mm <= 59
0 <= SS <= 59

마지막 저축시간이 9999년을 초과하는 입력은 주어지지 않음
'''

class Solution:
    def solve(self, s: str, times: List[int]) -> List[int]:
        # Time Complexity :  
        # Space Complexity : 

        if len(times) == 0:
            return [0, 0]

        splited_s = s.split(':')
        y, month, d, h, m, second = splited_s
        month = int(month) + int(y) * 12
        d = int(d) + 30 * month
        h = int(h) + 24 * d
        m = int(m) + 60 * h
        init_second = int(second) + 60 * m
        started_second = init_second

        def time_to_second(str_time):
            dd, hh, mm, ss = str_time.split(':')
            hh = int(hh) + int(dd) * 24
            mm = int(mm) + hh * 60
            ss = int(ss) + mm * 60

            return ss

        saved_day = init_second // (60 * 60 * 24)
        flag = 1 # is saved every day?

        for each_time in times:
            next_save_second = time_to_second(each_time)

            init_second += next_save_second
            if flag == 1:
                next_save_day = init_second // (60 * 60 * 24)
                if next_save_day - saved_day <= 1:
                    saved_day = next_save_day
                else:
                    flag = 0

        start_date = started_second // (60 * 60 * 24)
        last_date = init_second // (60 * 60 * 24)

        return [flag, last_date - start_date + 1]
        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            s: str
            times: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(
                    s = '2021:04:12:16:06:35',
                    times = ['01:06:30:00','01:04:12:00']),
                expect=[0,4] # 1일 1저축 실패. 저축 기간은 4월 12~15일 총 4일
            ),
            TestCase(
                name="test 2",
                input=Args(
                    s = '2021:04:12:16:06:35',
                    times = ['01:06:30:00','00:01:12:00']),
                expect=[1,2] # 4월 12, 13일 저축. 이틀간, 1일 1저축 성공
            ),
            TestCase(
                name="test 3",
                input=Args(
                    s = '2021:04:12:16:10:42',
                    times = ['01:06:30:00']),
                expect=[1,2] # 4월 12, 13일 저축. 이틀간, 1일 1저축 성공
            ),
            TestCase(
                name="test 4",
                input=Args(
                    s = '2021:04:12:16:08:35',
                    times = ['01:06:30:00','01:01:12:00','00:00:09:25']),
                expect=[1,4] # 4월 12일 ~ 15일 저축. 4일간 1일 1저축 성공
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(s=c.input.s, times=c.input.times)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
