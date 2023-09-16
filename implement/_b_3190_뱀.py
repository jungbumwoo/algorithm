# https://www.acmicpc.net/problem/3190

'''
5
0
5
4 D
8 D
12 D
15 D
20 L

ans: 20

---

8
3
5 4
5 8
2 5
6
7 D
11 D
15 D
18 D
19 D
20 D

ans: 21

---

8
5
6 1
7 3
3 5
5 7
5 6
12
2 D
8 D
10 D
12 D
18 L
20 L
22 L
24 L
25 L
28 L
32 D
33 L

ans: 27

---
tc4

20
13
6 15
7 18
20 14
14 13
11 9
7 10
3 18
10 10
13 13
13 5
6 9
10 4
4 3
19
17 D
36 D
41 D
54 D
56 L
57 L
63 L
68 L
72 L
73 L
76 D
79 D
82 D
85 D
87 D
93 L
105 D
110 D
114 D

ans: 90

---
tc5

35
28
21 2
22 23
3 5
34 30
29 31
3 28
20 12
27 26
31 7
5 10
21 10
19 2
15 23
4 23
3 19
3 35
13 30
30 30
23 27
32 17
22 24
8 27
4 8
30 18
15 28
22 29
28 5
16 33
20
27 D
61 L
68 L
100 L
133 L
160 L
165 D
168 D
170 D
182 D
206 D
207 D
214 D
215 D
216 L
237 D
240 D
241 L
251 D
252 D

ans: 237

--

tc6

58
58
31 50
13 34
54 27
21 40
17 36
28 48
38 27
13 51
53 44
28 57
10 25
26 20
29 31
2 6
53 24
19 45
31 58
30 36
2 33
52 31
22 30
15 56
44 36
26 12
47 18
10 57
4 5
28 52
6 30
48 15
5 38
25 38
29 48
50 40
36 5
35 15
45 9
56 42
18 15
51 9
33 29
26 47
46 28
43 29
16 41
16 30
38 35
49 14
20 7
39 50
21 36
40 25
9 5
6 4
49 23
15 32
41 4
42 2
78
5 D
8 D
10 L
15 L
17 L
18 L
20 L
32 L
64 D
65 L
76 D
81 L
82 D
86 L
87 D
88 L
91 L
94 D
100 D
103 D
107 D
109 L
110 D
111 D
115 D
116 L
117 D
118 D
119 L
120 L
121 D
143 D
192 D
229 D
276 L
287 L
313 L
365 D
366 D
403 L
404 L
439 D
440 D
463 L
464 L
469 D
470 L
482 D
493 D
494 D
498 L
510 L
513 D
514 L
519 L
520 D
529 L
545 L
552 D
558 D
564 D
565 D
568 L
570 L
574 D
576 D
581 D
588 D
597 D
619 D
672 D
678 D
693 D
742 L
743 L
747 D
748 L
751 L

ans: 586


'''
import sys
from collections import deque

N = int(sys.stdin.readline()) # size of boards
boards = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]


K = int(sys.stdin.readline()) # position of apples
apples = set()
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    # boards[a-1][b-1] = 1
    apples.add((a-1, b-1))

direction_guide = []
direction_flag = 0
L = int(sys.stdin.readline()) # info of chaging directions
for _ in range(L):
    S, D = sys.stdin.readline().split()
    S = int(S)

    direction_guide.append((S, D))

def get_direction(sec, ex_direction, direction_flag):
    if direction_flag == len(direction_guide): # there is no more direction change. JB, You have to take care out of index issue when you use array.
        return ex_direction, direction_flag

    if sec < direction_guide[direction_flag][0]:
        return ex_direction, direction_flag
    
    if sec == direction_guide[direction_flag][0]:

        if direction_guide[direction_flag][1] == 'D':
            if ex_direction == 'b':
                return 'd', direction_flag + 1
            elif ex_direction == 'd':
                return 'n', direction_flag + 1
            elif ex_direction == 'n':
                return 's', direction_flag + 1
            elif ex_direction == 's':
                return 'b', direction_flag + 1
            
        elif direction_guide[direction_flag][1] == 'L':
            if ex_direction == 'b':
                return 's', direction_flag + 1
            elif ex_direction == 's':
                return 'n', direction_flag + 1
            elif ex_direction == 'n':
                return 'd', direction_flag + 1
            elif ex_direction == 'd':
                return 'n', direction_flag + 1

        raise ValueError("Unexpected direction 1")
    
    raise ValueError("Unexpected Case 0")

# print(apples)
def game():
    queue = deque()
    body = set()
    # direction_to_nums = {'s': (-1, 0), 'b': (0, -1), 'n': (0, 1), 'd':(1, 0)} <- wrong again jb. 
    direction_to_nums = {'s': (0, -1), 'b': (-1, 0), 'n': (1, 0), 'd':(0, 1)}

    queue.append((0, 0, 'd', True)) # x, y, derection, is_head

    spent = 0
    direction_flag = 0

    while True:
        # print("================================")
        # print(f"queue: {queue}")        
        warm = []
        while queue:
            node = queue.popleft()
            warm.append(node)

        # print(f"warm: {warm}, body: {body}")

        ex, ey = 0, 0
        is_apple_eated = False
        for i in range(len(warm)):
            x, y, direction, is_head = warm[i][0], warm[i][1], warm[i][2], warm[i][3]
            # print(f"x: {x}, y: {y}, direction: {direction}, is_head: {is_head}")

            if is_head:
                new_direction, new_direction_flag = get_direction(spent, direction, direction_flag)
                # print(f"direction_to_nums: {direction_to_nums}, new_direction: {new_direction_flag}")
                nx, ny = x + direction_to_nums[new_direction][0], y + direction_to_nums[new_direction][1]

                if (nx, ny) in body:
                    return spent + 1
                
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    return spent + 1
                
                if (nx, ny) in apples:
                    is_apple_eated = True
                    apples.remove((nx, ny))
                
                # for next step
                direction_flag = new_direction_flag
                ex, ey = x, y
                queue.append((nx, ny, new_direction, is_head))

                if is_apple_eated and len(warm) == 1:
                    queue.append((x, y, None, False))
                    body.add((x, y))
            else:

                if i == (len(warm) - 1) and is_apple_eated is False: # JB, i must be compare with len - 1. not len.
                    body.remove((x, y))
    
                body.add((ex, ey))
                queue.append((ex, ey, None, False))
                ex, ey = x, y

                if i == (len(warm)-1) and is_apple_eated is True:
                    queue.append((x, y, None, False))
        
        spent += 1

print(game())




