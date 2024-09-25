# TODO: fix

# first try: recursion exceeded
import sys
sys.setrecursionlimit(10 ** 7)

class Solution:
    def reachNumber(self, target: int) -> int:
        """
        :type target: int
        :rtype: int
        """
        return self.find(target=target, current=0, step=0)

    @lru_cache
    def find(self, target, current, step):
        if target == current:
            return step

        return min(self.find(target, current + (step + 1), step + 1), 
        self.find(target, current - (step + 1), step + 1))


# second try: memory exceeded
from collections import deque

class Solution:
    def reachNumber(self, target: int) -> int:
        """
        :type target: int
        :rtype: int
        """

        queue = deque()
        queue.append((0, 0))

        while queue:
            q = queue.popleft()
            value, step = q[0], q[1]
        
            if value == target:
                return step

            next_step = step + 1

            queue.append(((value + next_step), next_step))
            queue.append(((value - next_step), next_step))
