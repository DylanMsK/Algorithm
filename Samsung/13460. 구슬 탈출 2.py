# url = 'https://www.acmicpc.net/problem/13460'

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for y in range(N):
    for x in range(M):
        if arr[y][x] == 'R':
            red = (x, y)
        elif arr[y][x] == 'B':
            blue = (x, y)

def find(cnt, rx, ry, bx, by):
    for i in range(4):
        nx, ny = rx+dx[i], ry+dy[i]
        if arr[ny][nx] == '#':
            continue
        if (nx, ny) == (bx, by):
            if arr[by+dy[i]][bx+dx[i]] == '#':
                continue
        q.append((cnt, i, (rx, ry), (bx, by)))


dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)

q = []
find(0, red[0], red[1], blue[0], blue[1])
print(q)
while q:
    cnt, d, red, blue = q.pop(0)