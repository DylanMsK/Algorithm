# url = 'https://www.acmicpc.net/problem/1002'

N = int(input())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

    if distance > r1 + r2:
        ip = 0
    elif distance == r1 + r2:
        ip = 1
    else:
        if distance == 0 and r1 == r2:
            ip = -1
        else:
            if distance + min(r1, r2) > max(r1, r2):
                ip = 2
            elif distance + min(r1, r2) == max(r1, r2):
                ip = 1
            else:
                ip = 0
    print(ip)
