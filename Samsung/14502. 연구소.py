# url = 'https://www.acmicpc.net/problem/14502'
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

viruses = []
empties = []
for y in range(N):
    for x in range(M):
        if arr[y][x] == 2:
            viruses.append((x, y))
        elif arr[y][x] == 0:
            empties.append((x, y))

max_ = 0
def spread(viruses, walls):
    global max_

    brr = deepcopy(arr)

    q = viruses[::]
    for x, y in walls:
        brr[y][x] = 1
    
    while q:
        x, y = q.pop(0)
        for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if brr[ny][nx]:
                continue
            brr[ny][nx] = 2
            q.append((nx, ny))

    cnt = 0
    for y in range(N):
        for x in range(M):
            if brr[y][x] == 0:
                cnt += 1
    
    if cnt > max_:
        max_ = cnt

for idx, walls in enumerate(combinations(empties, 3)):
    spread(viruses, walls)

print(max_)