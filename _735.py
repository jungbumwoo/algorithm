# https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remains = asteroids
        while True:
            temp = []

            for a in remains:
                if len(temp) == 0:
                    temp.append(a)
                    continue

                if a < 0 and temp[-1] > 0:
                    if abs(temp[-1]) == abs(a):
                        temp.pop()
                    else: 
                        temp[-1] = a if abs(a) > abs(temp[-1]) else temp[-1]
                else:
                    temp.append(a)

            if len(temp) == len(remains):
                break

            remains = temp 

        return remains