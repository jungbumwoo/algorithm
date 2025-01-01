from collections import defaultdict, deque

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        cnt = [0] * len(quiet)
        candidates = set(i for i in range(len(quiet)))
        ans = [i for i in range(len(quiet))]
        data = defaultdict(list)

        for k in range(len(quiet)):
            candidates.add(k)

        queue = deque()

        for i in range(len(richer)):
            more, less = richer[i][0], richer[i][1]
            cnt[less] += 1
            if less in candidates:
                candidates.remove(less)
            data[more].append(less)

        for c in candidates:
            queue.append(c)

        while queue:
            node = queue.popleft()

            for j in range(len(data[node])):
                less_then = data[node][j]

                if quiet[ans[less_then]] > quiet[ans[node]]:    
                    ans[less_then] = ans[node]
                
                cnt[less_then] -= 1
                if cnt[less_then] == 0:
                    queue.append(less_then)

        return ans