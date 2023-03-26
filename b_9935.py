# https://www.acmicpc.net/problem/9935

'''
input_1)
mirkovC4nizCC44
C4

input_2)
12ab112ab2ab

bbbbbbbbbb
12ab

12a
'''
import sys
data = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

B = len(bomb)
bomb_last = bomb[len(bomb) - 1]

stack = [i for i in data[:B -1]]
for i in range(B - 1, len(data)):
    if bomb_last == data[i]:
        idx = len(stack) - (B - 1)
        if idx >= 0 and ''.join(stack[idx:]) + data[i] == bomb:
            del stack[idx:]
            continue
        
    stack.append(data[i])

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))
