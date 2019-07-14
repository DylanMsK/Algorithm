# url = 'https://www.acmicpc.net/problem/14503'

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def check_clean(nx, ny):
    global cnt
    if ny < 0 or ny >= N or nx < 0 or nx >= M:
        return False
    if arr[ny][nx]:
        return False
    cnt += 1
    return True


q = [(r, c, d)]
cnt = 1
while 1:
    y, x, d = q.pop(0)
    arr[y][x] = 2

    flag = False
    if d == 0:
        for dx, dy, nd in (-1, 0, 3), (0, 1, 2), (1, 0, 1), (0, -1, 0):
            ny, nx = y+dy, x+dx
            if check_clean(nx, ny):
                flag = True
                q.append((ny, nx, nd))
                break
        else:
            ny = y+1
            if ny < N:
                if arr[ny][x] == 1:
                    break
                q.append((ny, x, d))
                continue
            else:
                break

    elif d == 1:
        for dx, dy, nd in (0, -1, 0), (-1, 0, 3), (0, 1, 2), (1, 0, 1):
            ny, nx = y+dy, x+dx
            if check_clean(nx, ny):
                flag = True
                q.append((ny, nx, nd))
                break
        else:
            nx = x-1
            if nx >= 0:
                if arr[ny][x] == 1:
                    break
                q.append((y, nx, d))
                continue
            else:
                break

    elif d == 2:
        for dx, dy, nd in (1, 0, 1), (0, -1, 0), (-1, 0, 3), (0, 1, 2):
            ny, nx = y+dy, x+dx
            if check_clean(nx, ny):
                flag = True
                q.append((ny, nx, nd))
                break
        else:
            ny = y-1
            if ny >= 0:
                if arr[ny][x] == 1:
                    break
                q.append((ny, x, d))
                continue
            else:
                break

    else:
        for dx, dy, nd in (0, 1, 2), (1, 0, 1), (0, -1, 0), (-1, 0, 3):
            ny, nx = y+dy, x+dx
            if check_clean(nx, ny):
                flag = True
                q.append((ny, nx, nd))
                break
        else:
            nx = x+1
            if nx < M:
                if arr[ny][x] == 1:
                    break
                q.append((y, nx, d))
                continue
            else:
                break
    
print(cnt)