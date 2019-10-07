def lotate(key):
    l = len(key)
    lotated = [[0]*l for _ in range(l)]
    for y in range(l):
        for x in range(l):
            lotated[l-1-x][y] = key[y][x]
    return lotated


def check(key, lock):



def solution(key, lock):
    answer = True
    for y in range(len(lock)-len(key)):
        for x in range(len(lock)-len(key)):
            flag = True
            for i in range(len(key)):
                for j in range(len(key)):
                    if lock[y+i][x+j] == 0:
                        if key[i][j] != 1:
                            flag = False
                if not flag:
                    break
            if flag:

    return answer