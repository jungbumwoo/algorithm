# https://leetcode.com/problems/number-of-recent-calls

from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()
        self.buffered = []

    def ping(self, t: int) -> int:
        cnt = 1
        while self.q:
            p = self.q.popleft()
            if p < t - 3000:
                continue

            cnt += 1
            self.buffered.append(p)
        
        for k in reversed(self.buffered):
            self.q.appendleft(k)
        
        self.buffered = []
        self.q.append(t)
        return cnt

