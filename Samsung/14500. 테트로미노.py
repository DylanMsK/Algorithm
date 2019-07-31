# url = 'https://www.acmicpc.net/problem/14500'

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def others(x, y, visited, sum_):
    global max_

    if len(visited) == 4:
        max_ = max(max_, sum_)
        return
    
    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if (nx, ny) in visited:
            continue
        others(nx, ny, visited+[(nx, ny)], sum_+arr[ny][nx])


blocks = [[(1, 0), (2, 0), (1, -1)],
          [(1, 0), (2, 0), (1, 1)],
          [(0, 1), (0, 2), (1, 1)],
          [(0, 1), (0, 2), (-1, 1)],
          [(-1, 0), (-2, 0), (-1, 1)],
          [(-1, 0), (-2, 0), (-1, -1)],
          [(0, -1), (0, -2), (1, -1)],
          [(0, -1), (0, -2), (-1, -1)]]
def fuck(x, y):
    global max_

    for block in blocks:
        sum_ = arr[y][x]
        flag = True
        for dx, dy in block:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                flag = False
                break
            sum_ += arr[ny][nx]

        if flag:
            max_ = max(max_, sum_)

max_ = 0
for y in range(N):
    for x in range(M):
        fuck(x, y)
        others(x, y, [(x, y)], arr[y][x])

print(max_)