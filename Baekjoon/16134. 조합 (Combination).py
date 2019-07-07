# url = 'https://www.acmicpc.net/problem/16134'

N, R = map(int, input().split())

res = 1
for i in range(N, N-R, -1):
    res *= i

for i in range(R, 1, -1):
    res //= i

print(res % 1000000007)