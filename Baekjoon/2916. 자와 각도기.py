# url = 'https://www.acmicpc.net/problem/2916'

N, K = map(int, input().split())
degrees = list(map(int, input().split()))
res = list(map(int, input().split()))
possible = [0]*360
possible[0] = 1
q = [0]

while q:
    degree = q.pop(0)
    for i in degrees:
        small, big = i-degree, i+degree
        if small < 0:
            small += 360
        if big >= 360:
            big -= 360

        if not possible[small]:
            possible[small] = 1
            q.append(small)
        if not possible[big]:
            possible[big] = 1
            q.append(big)

for i in res:
    if possible[i]:
        print('YES')
    else:
        print('NO')


