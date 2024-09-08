# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if i + 1 < len(flowerbed):
                    flowerbed[i+1] = 2
            
            if flowerbed[i] == 0:
                if i + 1 < len(flowerbed) and flowerbed[i+1] == 0:
                    flowerbed[i+1] = 2
                    cnt += 1
                if i == len(flowerbed) - 1:
                    cnt += 1
            
            if cnt >= n:
                return True
        return False