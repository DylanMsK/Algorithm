# url = 'https://www.acmicpc.net/problem/11051'

N, K = map(int, input().split())
if K == 0:
    print(1)
else:
    res = 1
    for i in range(N, N-K, -1):
        res *= i
    for i in range(1, K+1):
        res //= i
    print(res%10007)