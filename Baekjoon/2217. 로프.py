# url = 'https://www.acmicpc.net/problem/2217'

N = int(input())

ropes = [int(input()) for _ in range(N)]
ropes.sort()
max_ = 0
for i in range(N):
    max_ = max((N-i) * ropes[i], max_)
print(max_)
