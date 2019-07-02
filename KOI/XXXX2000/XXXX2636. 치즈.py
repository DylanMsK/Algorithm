# url = 'https://www.acmicpc.net/problem/2636'

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = []

def init():
    global q
    temp = []
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                temp.append((0, y, x))
                break
    
    for y in range(N-1, -1, -1):
        for x in range(M-1, -1, -1):
            if arr[y][x] == 1:
                temp.append((0, y, x))
                break
    
    for x in range(M):
        for y in range(N):
            if arr[y][x] == 1:
                temp.append((0, y, x))
                break

    for x in range(M-1, -1, -1):
        for y in range(N-1, -1, -1):
            if arr[y][x] == 1:
                temp.append((0, y, x))
                break
    q.append(list(set(temp)))

init()
cnt = 0
while q[0]:
    cheeses = q.pop(0)
    cnt = len(cheeses)
    nxt = []
    print()
    for y in arr:
        print(y)

    while cheeses:
        t, y, x = cheeses.pop(0)
        arr[y][x] = 0
        for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
            nt, ny, nx = t+1, y+dy, x+dx
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if arr[ny][nx] == 0:
                continue
            nxt.append((nt, ny, nx))

    nxt = list(set(nxt))
    q.append(nxt)
    
print(cnt)
print(t)
    