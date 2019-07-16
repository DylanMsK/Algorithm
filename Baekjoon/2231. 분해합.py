# url = 'https://www.acmicpc.net/problem/2231'

N = int(input())
res = 0
for i in range(1, N+1):
    tot = i
    n_str = str(i)
    for j in n_str:
        tot += int(j)
    if tot == N:
        res = i
        break
print(res)
