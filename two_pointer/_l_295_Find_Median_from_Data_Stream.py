import heapq

# wrong: heapq 에 정렬 순을 배열처럼 indexing 불가능함.

import heapq

class MedianFinder:
    def __init__(self):
        self.count = 0
        self.queue = []
        heapq.heapify(self.queue)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.queue, num)
        self.count += 1

    def findMedian(self) -> float:
        if self.count == 0:
            return 0
        
        if self.count % 2 == 0:
            first = self.queue[(self.count // 2)-1]
            second = self.queue[(self.count // 2)]
            return (first + second) / 2
        else:
            return self.queue[self.count // 2]
        