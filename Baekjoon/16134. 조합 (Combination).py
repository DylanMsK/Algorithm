# url = 'https://www.acmicpc.net/problem/16134'

def combination(N, R):
    res = 1
    for i in range(N, N-R, -1):
        res *= i

    for i in range(2, R+1):
        res //= i
    return res

N, R = map(int, input().split())

res = 0
for i in range(R-1, N):
    if res > 1000000007:
        break
    res += combination(i, R-1)

print(res)