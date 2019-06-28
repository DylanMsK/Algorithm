# url = 'https://www.acmicpc.net/problem/16236'

from heapq import heappop, heappush

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = []

for y in range(N):
    for x in range(N):
        if arr[y][x] == 9:
            # q.append((0, y, x))
            heappush(q, (0, y, x))
            arr[y][x] = 0
            break

body, eat, tot = 2, 0, 0
path = [[False]*N for _ in range(N)]
while q:
    # d, y, x = q.pop(0)
    d, y, x = heappop(q)
    if 0 < arr[y][x] < body:
        eat += 1
        arr[y][x] = 0
        if eat == body:
            body += 1
            eat = 0
        tot += d
        d = 0
        q = []
        # while q:
        #     q.pop()
        path = [[False]*N for _ in range(N)]

    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nd, ny, nx = d+1, y+dy, x+dx
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if 0 < arr[ny][nx] > body or path[ny][nx]:
            continue
        path[ny][nx] = True
        # q.append((nd, ny, nx))
        heappush(q, (nd, ny, nx))
    
print(tot)