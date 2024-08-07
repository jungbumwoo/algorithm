# fixme: 72.0 / 100

def solution(scores):
    if len(scores) == 1:
        return 1
    
    target_left, target_right = scores[0][0], scores[0][1]
    
    sorted_left_high_scores = sorted(scores, key=lambda x: (-x[0], -x[1]))
    left_high_scores = []
    left_high_scores.append(sorted_left_high_scores[0])
    
    for i in range(1, len(sorted_left_high_scores)):
        if sorted_left_high_scores[i][0] < left_high_scores[0][0] and sorted_left_high_scores[i][1] < left_high_scores[0][1]:
            continue
        left_high_scores.append(sorted_left_high_scores[i])
    
    sorted_right_high_scores = sorted(left_high_scores, key=lambda x: (-x[1], -x[0]))
    right_high_scores = []
    right_high_scores.append(sorted_right_high_scores[0])
    
    for i in range(1, len(sorted_right_high_scores)):
        if sorted_right_high_scores[i][0] < right_high_scores[0][0] and sorted_right_high_scores[i][1] < right_high_scores[0][1]:
            continue
        right_high_scores.append(sorted_right_high_scores[i])
        
    final = sorted(right_high_scores, key=lambda x: -(x[0] + x[1]))
    
    for k in range(len(final)):
        if final[k][0] == target_left and final[k][1] == target_right:
            return k + 1
    
    return -1