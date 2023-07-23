import sys

'''
2
< >

9
> < < < > > > < <
'''

N = int(sys.stdin.readline())
data = list(map(str, sys.stdin.readline().rstrip().split()))
is_used = [False] * 10
print(is_used)
print(data)


def select(index: int, pivot: int, rangee: str):
    if i > N + 1:
        return

    if rangee == ">":

        for k in range(pivot, 10):
            if is_used[k]:
                continue

            

    
select(0, 9, "<") or select(0, 0, ">")
    
    
