# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0

        queue = s[:]
        heapq.heapify(queue)

        index = 0
        cnt = 0
        g.sort()

        while queue:
            cookie = queue.pop()

            if cookie >= g[index]:
                cnt += 1
                index += 1

                if index == len(g):
                    return cnt
        
        return cnt 