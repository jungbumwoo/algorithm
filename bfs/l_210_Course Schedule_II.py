from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        board = defaultdict(set)
        count = [0] * numCourses
        for pair in prerequisites:
            second, first = pair[0], pair[1]
            board[first].add(second)
            count[second] += 1

        queue = deque()

        for i in range(numCourses):
            if count[i] == 0:
                queue.append(i)
        ans = []

        while queue:
            k = queue.popleft()

            for v in board[k]:
                count[v] -= 1

                if count[v] == 0:
                    queue.append(v)
                
            ans.append(k)
        
        if len(ans) != numCourses:
            return []
        return ans