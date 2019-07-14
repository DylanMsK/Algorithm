# url = 'https://www.acmicpc.net/problem/14503'

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

bfs = {
    0: [(-1, 0, 3), (0, 1, 2), (1, 0, 1), (0, -1, 0)],
    1: [(0, -1, 0), (-1, 0, 3), (0, 1, 2), (1, 0, 1)],
    2: [(1, 0, 1), (0, -1, 0), (-1, 0, 3), (0, 1, 2)],
    3: [(0, 1, 2), (1, 0, 1), (0, -1, 0), (-1, 0, 3)]
}
back = {
    0: (1, 0),
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1)
}

def check_clean(x, y):
    global cnt
    if y < 0 or y >= N or x < 0 or x >= M or arr[y][x]:
        return False
    cnt += 1
    return True


q = [(r, c, d)]
cnt = 1
while 1:
    y, x, d = q.pop(0)
    arr[y][x] = 2
    for dx, dy, nd in bfs[d]:
        ny, nx = y+dy, x+dx
        if check_clean(nx, ny):
            q.append((ny, nx, nd))
            break
    else:
        ny, nx = y+back[d][0], x+back[d][1]
        if ny >= 0 or ny < N or nx >= 0 or nx < M:
            if arr[ny][nx] == 1:
                break
            q.append((ny, nx, d))
        else:
            break

print(cnt)
