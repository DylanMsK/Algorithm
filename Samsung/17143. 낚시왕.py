# url = 'https://www.acmicpc.net/problem/17143'

def fish(me):
    global sharks, weight
    sharks.sort(key=lambda x: (x[1], x[0]))
    nxt = []
    while sharks:
        shark = sharks.pop(0)
        if shark[1] < me:
            nxt.append(shark)
            continue
        elif shark[1] == me:
            weight += shark[-1]
            break
        else:
            nxt.append(shark)
            break
    if sharks:
        nxt.extend(sharks)
    
    return nxt


def move():
    global sharks

    arr = [[[]]*C for _ in range(R)]
    while sharks:
        shark = sharks.pop(0)
        r, c, s, d = tuple(shark[:-1])
        dx, dy = 0, 0
        while s:
            s -= 1
            if d == 1:
                dy = -1
                if 1 <= r + dy:
                    r -= 1
                else:
                    d = 2
                    r += 1
            elif d == 2:
                dy = 1
                if r + dy <= R:
                    r += 1
                else:
                    d = 1
                    r -= 1
            elif d == 3:
                dx = 1
                if c + dx <= C:
                    c += 1
                else:
                    d = 4
                    c -= 1
            else:
                dx = -1
                if 1 <= c + dx:
                    c -= 1
                else:
                    d = 3
                    c += 1
            # print(r, c, s, type(d))
        if arr[r-1][c-1]:
            if shark[-1] > arr[r-1][c-1][-1]:
                arr[r-1][c-1] = [r, c, shark[2], d, shark[-1]]
        else:
            arr[r-1][c-1] = [r, c, shark[2], d, shark[-1]]
    nxt = []
    for y in range(R):
        for x in range(C):
            if arr[y][x]:
                nxt.append(arr[y][x])
    return nxt


R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]    # (r, c), 속력, 방향, 크기
me = 0
weight = 0
while me <= C:
    me += 1
    sharks = fish(me)
    if me == C:
        break
    sharks = move()

print(weight)