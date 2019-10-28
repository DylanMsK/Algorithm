# url = 'https://www.acmicpc.net/problem/13717'

N = int(input())
cnt = 0
max_ = 0
for _ in range(N):
    name = input()
    K, M = map(int, input().split())
    evol = 0
    while K <= M:
        M -= K
        M += 2
        evol += 1
    cnt += evol
    if evol > max_:
        max_ = evol
        max_name = name

print(cnt)
print(max_name)