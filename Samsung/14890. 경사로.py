# url = 'https://www.acmicpc.net/problem/14890'

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def check(lst):
    i = 0
    stack = 1
    now = lst[i]
    while i < N-1:
        i += 1
        diff = now - lst[i]
        if diff > 1 or diff < -1:
            return False
        elif diff == 1:
            if i+L > N:
                return False
            for j in range(i+1, i+L):
                if now - lst[j] != 1:
                    return False
            stack = 1-L
        elif diff == -1:
            if i-L < 0 or stack < L:
                return False
            stack = 1
        else:
            stack += 1

        now = lst[i]
    return True

cnt = 0
for row in arr:
    if check(row):
        cnt += 1

for y in range(N):
    for x in range(N):
        if x > y:
            arr[y][x], arr[x][y] = arr[x][y], arr[y][x]

for row in arr:
    if check(row):
        cnt += 1
    
print(cnt)