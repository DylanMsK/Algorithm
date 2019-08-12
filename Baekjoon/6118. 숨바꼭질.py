# url = 'https://www.acmicpc.net/problem/6118'

N, M = map(int, input().split())
cabins = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    cabins[a].append(b)
    cabins[b].append(a)

visited = [0] * (N+1)
d, now = 0, [1]
visited[1] = 1
while 1:
    nxt = []
    for i in now:
        for j in cabins[i]:
            if visited[j]:
                continue
            nxt.append(j)
            visited[j] = 1
    if nxt:
        now = nxt
        d += 1
    else:
        print(min(now), d, len(now))
        break

