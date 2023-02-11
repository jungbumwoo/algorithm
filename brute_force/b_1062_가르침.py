import sys
import copy
from itertools import combinations
'''
3 6
antarctica
antahellotica
antacartica
'''

required = {"a", "n", "t", "i", "c"}

N, K = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().rstrip()[4:-4] for _ in range(N)]

combi = []
temp = set()
def select(how_many, cnt, idx): # idx 0 ~ 25
    if how_many == cnt:
        # copied = copy.deepcopy(temp)
        combi.append(temp)
        return 

    for p in range(idx+1, 26):
        if chr(97 + p) not in temp: 
            temp.add(chr(97 + p))
            select(how_many+1, cnt, p)
            temp.remove(chr(97 + p))
items = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
if K > 5 and K < 26:
    num = K - 5
    # select(0, num, -1) # 아직, num, -1
    combi = list(combinations(items, num))
    answer = 0

    for learned in combi:
        # print(f'learned: {learned}')
        cnt = 0
        for word in words:
            # print(f'word: {word}')
            is_learned = True
            for alpha in word:
                # print(alpha, end=' ')
                # print('')
                if alpha in required:
                    # print(f'{alpha} is required. pass', end=' /')
                    continue

                if alpha not in learned:
                    is_learned = False
                    break

            if is_learned:
                cnt += 1
        
        answer = max(answer, cnt) 
    
    print(answer)
elif K < 5:
    print(0)
elif K == 5:
    answer = 0
    cnt = 0
    for word in words:
        # print(f'word: {word}')
        is_learned = True
        for alpha in word:

            if alpha not in required:
                is_learned = False
                break
        if is_learned:
            cnt += 1
    
    answer = max(answer, cnt) 
    
    print(answer)
else:
    print(N)
            

        
    