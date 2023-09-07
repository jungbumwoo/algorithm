import sys
sys.setrecursionlimit(10 ** 7)

# bottom - up 으로 다시 풀어보기 

'''
5
1 5 2 3 7
'''

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().rstrip().split()))
cache = {}

def select(index, weight):
    if index == len(data):
        return 0
    
    if (index, weight) in cache:
        return cache[(index, weight)]

    a, b = 0, 0
    if data[index] > weight:
        # selected
        a = select(index + 1, data[index]) + 1

    # not selected
    b = select(index + 1, weight)

    ans = max(a, b)
    cache[(index, weight)] = ans
    return ans

print(select(0, 0))