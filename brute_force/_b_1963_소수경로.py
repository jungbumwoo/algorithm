# https://www.acmicpc.net/problem/1963
# fix me: 재귀초과 


import functools
import sys
sys.setrecursionlimit(10**4)

N = int(sys.stdin.readline())

@functools.lru_cache(maxsize=None)
def is_sosu(num: int) -> bool:
    if num <= 3:
        return False
    
    k = 2
    while True:
        if num % k == 0:
            return False
        
        k += 1
        if k * k > num:
            break

    return True

@functools.lru_cache(maxsize=None)
def search(i: int, target: int):
    
    if i == target:
        return 1
    
    temp = 10 ** 7

    for p in range(0, 4):
        str_int = list(str(i))
        print('here')
        # str[0]
        # convert num
        for j in range(0, 10):
            dummy = str(j)
            str_int[p] = dummy
            converted = int(''.join(str_int))

            if converted > 1000 and (i != converted) and is_sosu(converted):
                temp = min(temp, search(converted, target))

    if temp == 10 ** 7:
        return 10 ** 7
    
    return temp + 1

for i in range(N):
    _from, to = map(int, sys.stdin.readline().split())
    result = search(_from, to)
    if result == 10 ** 7:
        print("Impossible")
    else:
        print(result)
