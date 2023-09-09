# https://www.acmicpc.net/problem/1562

import sys
import functools

N = int(sys.stdin.readline())

flag = (1 << 10) - 1

def up_bit(bits, value):
    mask = 1 << value
    return mask | bits

def down_bit(bits, value):
    mask = ~(1 << value)
    return mask & bits

@functools.lru_cache(maxsize=None)
def select(index, value, bits):
    # print(index, value, bits)
    global flag

    if index == N:
        if bits == flag:
            return 1
        return 0

    ans = 0
    if value == 9:
        bits = up_bit(bits, value-1)
        ans += select(index+1, value-1, bits)
        bits = down_bit(bits, value-1)
    elif value == 0:
        bits = up_bit(bits, value+1)
        ans += select(index+1, value+1, bits)
        bits = down_bit(bits, value+1)
    else:
        bits = up_bit(bits, value+1)
        ans += select(index+1, value+1, bits)
        bits = down_bit(bits, value+1)

        bits = up_bit(bits, value-1)
        ans += select(index+1, value-1, bits)
        bits = down_bit(bits, value-1)
        
    return ans

result = 0
for k in range(1, 10):
    result += select(0, k, 1 << k)

result = result % 1000000000
print(result)
