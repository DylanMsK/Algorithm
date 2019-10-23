# url = 'https://www.acmicpc.net/problem/1476'

E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
cnt = 1
while e != E or s != S or m != M:
    cnt += 1
    if 1 <= e < 15:
        e += 1
    else:
        e = 1
    if 1 <= s < 28:
        s += 1
    else:
        s = 1
    if 1 <= m < 19:
        m += 1
    else:
        m = 1
print(cnt)