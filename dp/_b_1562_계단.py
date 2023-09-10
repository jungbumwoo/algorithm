# https://www.acmicpc.net/problem/1562

'''
1. bit visited 처리 시 bit 특성 상 이전 방문내역까지 지워져버리는 문제 캐치하지 못함
2. dfs return 조건인 index 처리 틀림
'''

import sys
import functools

N = int(sys.stdin.readline())

flag = (1 << 10) - 1

def up_bit(bits, value):
    mask = 1 << value
    return mask | bits

@functools.lru_cache(maxsize=None)
def select(index, value, bits):
    global flag

    if index == N - 1:
        if bits == flag:
            return 1
        return 0

    ans = 0
    if value == 9:
        next_bit = up_bit(bits, value-1)
        ans += select(index+1, value-1, next_bit)
    elif value == 0:
        next_bit = up_bit(bits, value+1)
        ans += select(index+1, value+1, next_bit)
    else:
        next_bit = up_bit(bits, value+1)
        ans += select(index+1, value+1, next_bit)
        
        next_bit = up_bit(bits, value-1)
        ans += select(index+1, value-1, next_bit)

    return ans

result = 0
for k in range(1, 10):
    result += select(0, k, 1 << k)

result = result % 1000000000
print(result)
