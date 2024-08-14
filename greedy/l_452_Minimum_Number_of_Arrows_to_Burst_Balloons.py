class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        arr = sorted(points, key=lambda x: (x[1], x[0]))

        cnt = 1
        ex = arr[0]
        for i in range(1, len(arr)):
            if arr[i][0] > ex[1]:
                cnt += 1
                ex = arr[i]
        return cnt

