# url = 'https://www.acmicpc.net/problem/14500'

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def others(x, y, visited, sum_):
    global max_

    if len(visited) == 4:
        if sum_ > max_:
            print(visited)
            max_ = sum_
        return
    
    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx, ny = x+dx, x+dy
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if (nx, ny) in visited:
            continue
        others(nx, ny, visited+[(nx, ny)], sum_+arr[ny][nx])

def fuck(x, y, sum_):
    global max_

max_ = 0
for y in range(N):
    for x in range(M):
        others(x, y, [(x, y)], arr[y][x])

print(max_)