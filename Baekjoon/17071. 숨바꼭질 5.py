# url = 'https://www.acmicpc.net/problem/17071'

N, K = map(int, input().split())
l = 500001
visited = [0]*l
visited[N] = 1
time = 0
q = [N]
while 1:
    if visited[K]:
        break

    time += 1
    nxt = []
    for i in q:
        for j in i, 1, -1:
            if 0 <= i+j < l and not visited[i+j]:
                nxt.append(i+j)
    nxt = list(set(nxt))
    for i in nxt:
        visited[i] = 1
    K += time
    
    if K >= l:
        break
    q = nxt

print(time) if K < l and visited[K] else print(-1)