# url = 'https://www.acmicpc.net/problem/1010'

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    tot = 1
    if N != M:
        for i in range(M, M-N, -1):
            tot *= i
        for i in range(N, 1, -1):
            tot //= i
    print(tot)