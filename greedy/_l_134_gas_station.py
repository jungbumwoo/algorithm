'''
fixme: timeout
time complexity: O(n^2)
시간 복잡도 개선하기
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [0] * len(gas)
        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
        
        for j in range(len(diff)):
            result = self.isValid(j, diff)
            if result is not False:
                return result

        return -1

    def isValid(self, k, diff):
        total = 0
        for p in range(k, k + len(diff)):
            index = p % len(diff)

            total += diff[index]
            if total < 0:
                return False    
        return k