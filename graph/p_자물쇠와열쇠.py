def rotate_key(key):
    return list(map(list, zip(*key[::-1])))

def search_hole(lock):
    hole_cnt = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                hole_cnt += 1

    return hole_cnt
    

def try_locking(p, q, key, lock, hole_cnt):
    # p, q - lock 기준
    # i, j - 키 기준
    for i in range(len(key)):
        for j in range(len(key[0])):
            nx = p + i
            ny = q + j

            if nx < 0 or ny < 0 or nx >= len(lock) or ny >= len(lock[0]):
                continue

            if lock[nx][ny] == 0 and key[i][j] == 1:
                hole_cnt -= 1
            elif lock[nx][ny] == 1 and key[i][j] == 1:
                return False

    if hole_cnt == 0:
        return True
    else:
        return False

def transform_lock(lock, key):
    data = [[-1] * (len(key[0]) * 2 + len(lock[0])) for _ in range((len(key)) * 2 + len(lock))]
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 1:
                data[i + len(key)][j + len(key[0])] = 1
            elif lock[i][j] == 0:
                data[i + len(key)][j + len(key[0])] = 0
    return data
    
def solution(key, lock):
    hole_cnt = search_hole(lock)
    lock = transform_lock(lock, key)
    for _ in range(4):
        key = rotate_key(key)

        for i in range(len(lock)):
            for j in range(len(lock)):

                if try_locking(i, j, key, lock, hole_cnt):
                    return True

    return False 
