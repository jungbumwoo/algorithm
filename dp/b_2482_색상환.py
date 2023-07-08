import sys
import functools

total = int(sys.stdin.readline())
cnt = int(sys.stdin.readline())

board = [None] * total
temp = [0]

span = total // cnt
s = total / cnt

print(f'span: {span}, s: {s}')

if s < 2:
    print(0)
    sys.exit()

# +1, span -1
@functools.lru_cache(maxsize=None)
def select(index):
    if index >= total:
        return 0
    
    if temp[0] == cnt:
        return 1
    
    t = 0
    for i in range(2, span + 1):
        
        temp[0] += 1
        t += select(index + i)
        temp[0] -= 1

    return t

print(select(-2))