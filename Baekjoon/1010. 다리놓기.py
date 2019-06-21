# url = 'https://www.acmicpc.net/problem/1010'

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    cnt = 1
    for i in range(N):
        # temp = 0
        for j in range(M-N, 0, -1):
            cnt += j
    print(cnt)