# url = 'https://www.acmicpc.net/problem/2636'

N, M = map(int, input().split())
arr = [[0]*(M+2)] + [[0] + list(map(int, input().split())) + [0]
                     for _ in range(N)] + [[0]*(M+2)]

cnt, time = 0, 0
while 1:
    nxt = []
    q = [(0, 0)]
    while q:
        y, x = q.pop(0)
        for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
            ny, nx = y+dy, x+dx
            if nx < 0 or nx >= M+2 or ny < 0 or ny >= N+2:
                continue
            if arr[ny][nx] == 0:
                arr[ny][nx] = -1
                q.append((ny, nx))
            if arr[ny][nx] == 1:
                arr[ny][nx] = -1
                nxt.append((ny, nx))

    if not nxt:
        break

    time += 1
    cnt = len(nxt)
    for y in range(N+2):
        for x in range(M+2):
            if arr[y][x] == -1:
                arr[y][x] = 0

print(f'{time}\n{cnt}')
