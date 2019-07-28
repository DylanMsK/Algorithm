# url = 'https://www.acmicpc.net/problem/17142'

from itertools import combinations

N, M = map(int, input().split())
arr = [[1]*(N+2)]
for i in range(N):
    arr.append([1] + list(map(int, input().split())) +[1])
arr.append([1]*(N+2))


walls, inactive = [], []
for y in range(1, N+1):
    for x in range(1, N+1):
        if arr[y][x] == 1:
            walls.append((x, y))
        elif arr[y][x] == 2:
            inactive.append((x, y))


min_ = 1e9
for comb in combinations(inactive, M):
    brr = [[0]*(N+2) for _ in range(N+2)]
    q = list(comb)
    cnt = 0
    while 1:
        nxt_q = []
        for x, y in q:
            brr[y][x] = 1
            for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
                nx, ny = x+dx, y+dy
                if arr[ny][nx] or brr[ny][nx]:
                    continue
                brr[ny][nx] = 1
                nxt_q.append((nx, ny))
        if nxt_q:
            cnt += 1
            q = nxt_q
        else:
            break
    min_ = min(min_, cnt)
print(min_)