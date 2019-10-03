# url = 'https://www.acmicpc.net/problem/9461'

tc = int(input())
P = [1, 1, 1, 2, 2] + [0]*(101-5)
for i in range(5, 101):
    P[i] = P[i-1] + P[i-5]

for _ in range(tc):
    print(P[int(input())-1])
