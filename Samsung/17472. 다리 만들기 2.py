# url = 'https://www.acmicpc.net/problem/17472'
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

def numbering_irlands(x, y):
    visited[y][x] = 1
    arr[y][x] = irland
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if not visited[ny][nx] and arr[ny][nx]:
                arr[ny][nx] = irland
                visited[ny][nx] = 1
                q.append((nx, ny))


irland = 1
for y in range(N):
    for x in range(M):
        if arr[y][x] and not visited[y][x]:
            numbering_irlands(x, y)
            irland += 1

min_distance = [[10**5]*irland for _ in range(irland)]

def find_min_distance(irland):
    dist = [[-1]*M for _ in range(N)]
    q = deque()
    for y in range(N):
        for x in range(M):
            if arr[y][x] == irland:
                q.append((x, y))
                dist[y][x] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if not dist[ny][nx]:
                continue
            else:
                distance = 1
                while 1:
                    nx += dx[i]
                    ny += dy[i]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N:
                        break
                    if not dist[ny][nx]:
                        break
                    if arr[ny][nx] and arr[ny][nx] != irland:
                        if distance > 1:
                            min_distance[arr[ny][nx]][irland] = min(min_distance[arr[ny][nx]][irland], distance)
                            min_distance[irland][arr[ny][nx]] = min(min_distance[irland][arr[ny][nx]], distance)
                        break
                    distance += 1
    return


for i in range(1, irland):
    find_min_distance(i)

costs = []
for i in range(1, irland):
    for j in range(1, irland):
        if i > j:
            if min_distance[i][j] != 10**5:
                costs.append((i, j, min_distance[i][j]))
costs.sort(key=lambda x: x[2])

price = 0
connected = [0]*irland
connected[0] = 1
connected[1] = 1
while sum(connected) != irland:
    for cost in costs:
        s, e, p = cost
        if connected[s] or connected[e]:
            if connected[s] and connected[e]:
                continue
            else:
                connected[s] = 1
                connected[e] = 1
                price += p
                break
    else:
        price = -1
        break

print(price)

