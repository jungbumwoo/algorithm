class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        data = []
        for i in range(len(difficulty)):
            data.append((difficulty[i], profit[i]))
        
        data.sort()
        difficulty.sort()

        cache = [0] * len(data)
        cache[0] = data[0][1]
        for j in range(1, len(data)):
            cache[j] = max(cache[j-1], data[j][1])
        
        result = 0
        for w in worker:
            result += self.find(w, difficulty, cache)

        return result
    
    def find(self, w, difficulty, cache):
        left, right = 0, len(difficulty)
        
        while left < right:
            mid = (left + right) // 2
            if w >= difficulty[mid]:
                left = mid + 1
            else:
                right = mid
        
        index = left - 1 if left -1 >= 0 else left
        return cache[index] if difficulty[index] <= w else 0               