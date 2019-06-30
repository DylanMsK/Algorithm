# url = 'https://www.acmicpc.net/problem/17086'

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
vacancies = []

def get_vacancies():
    global vacancies
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 0:
                vacancies.append((0, y, x))

def bfs():
    max_ = 0
    while vacancies:
        q = [vacancies.pop(0)]
        check = [[0]*M for _ in range(N)]
        while q:
            d, y, x = q.pop(0)
            if arr[y][x]:
                if d > max_:
                    max_ = d
                break
            
            for dx, dy in (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1):
                nd, ny, nx = d+1, y+dy, x+dx
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if check[ny][nx]:
                    continue
                q.append((nd, ny, nx))
                check[ny][nx] = 1
    print(max_)

get_vacancies()
bfs()