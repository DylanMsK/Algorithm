# url = 'https://www.acmicpc.net/problem/15685'

N = int(input())
curves = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*101 for _ in range(101)]

directions = {
    0: (1, 0),
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1)
}

def rotation(x, y, ex, ey):
    dx, dy = x-ex, y-ey
    nx, ny = ex-dy, ey+dx
    return nx, ny

while curves:
    x, y, d, g = curves.pop(0)
    arr[y][x] = 1
    gen = 0
    q = [(x, y), (x+directions[d][0], y+directions[d][1])]
    arr[q[1][1]][q[1][0]] = 1

    while gen < g:
        ex, ey = q[-1]
        nq = []
        for x, y in q[:-1][::-1]:
            nx, ny = rotation(x, y, ex, ey)
            nq.append((nx, ny))
            if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:
                continue
            arr[ny][nx] = 1
        q += nq
        gen += 1

cnt = 0
for y in range(100):
    for x in range(100):
        if arr[y][x] and arr[y+1][x] and arr[y][x+1] and arr[y+1][x+1]:
            cnt += 1

print(cnt)