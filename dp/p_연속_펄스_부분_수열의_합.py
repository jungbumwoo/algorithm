# https://school.programmers.co.kr/learn/courses/30/lessons/161988
def solution(sequence):
    answer = 0
    
    data = [[0, 0] for _ in range(len(sequence))]
    
    data[-1][0], data[-1][1] = sequence[-1], -1 * sequence[-1]
    answer = max(data[-1][0], data[-1][1])
    for i in range(len(sequence)-2, -1, -1):
        data[i][0] = max(sequence[i], sequence[i] + data[i+1][1])
        data[i][1] = max(-1 * sequence[i], -1 * sequence[i] + data[i+1][0])
        
        answer = max(answer, data[i][0], data[i][1])
    
    return answer