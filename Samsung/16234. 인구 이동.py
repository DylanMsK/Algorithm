# url = 'https://www.acmicpc.net/problem/16234'

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def find_unions():
    brr = [[0]*N for _ in range(N)]
    unions = {}
    n = 1
    for y in range(N):
        for x in range(N):
            if brr[y][x] == 0:
                q = [(x, y, arr[y][x])]
                idx = 0
                brr[y][x] = 1
                while 1:
                    x, y, p = q[idx]
                    for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
                        nx, ny = x+dx, y+dy
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if brr[ny][nx] or abs(p - arr[ny][nx]) < L or abs(p - arr[ny][nx]) > R:
                            continue
                        brr[ny][nx] = 1
                        q.append((nx, ny, arr[ny][nx]))
                    if idx == len(q)-1:
                        break
                    idx += 1

                if idx:
                    unions[n] = q
                    n += 1
    if unions:
        return unions
    return

cnt = 0
while 1:
    unions = find_unions()
    if unions:
        cnt += 1
        for n in unions:
            union = unions[n]
            sum_, length = sum([c[2] for c in union]), len(union)
            p = int(sum_ / length)
            for country in union:
                x, y, _ = country
                arr[y][x] = p
        print(unions)
        for i in arr:
            print(i)
    else:
        break

print(cnt)
