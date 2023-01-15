# https://school.programmers.co.kr/learn/courses/30/lessons/43162

'''
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
'''

# 플루이드-와샬로 푸는 풀이도 있음.

def solution(n, computers):
    data = []
    def find(k):
        if k == data[k]:
            return k
        return find(data[k])
    
    def union(a, b):
        a_parent = find(a)
        b_parent = find(b)
        if a_parent < b_parent:
            data[b_parent] = a_parent
            parent = a_parent
        else:
            data[a_parent] = b_parent
            parent = b_parent
        return parent
    
    for p in range(n):
        data.append(p)
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and data[i] != data[j]:
                new_parent = union(i, j)
                data[i] = new_parent
    cnt = set()
    
    for q in range(len(data)):
        parent = find(q)
        if parent not in cnt:
            cnt.add(parent)
    
    return len(cnt)