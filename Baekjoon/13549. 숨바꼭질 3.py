# url = 'https://www.acmicpc.net/problem/13549'

N, K = map(int,input().split())

visited = [0]*100001
q = []
for i in range(N, 100001, N):
    visited[i] = 1
    q.append(i)
time = 0
while 1:
    if visited[K]:
        break
    nxt = []
    for i in q:
        if i > K:
            if 0 <= i-1 < 100001 and not visited[i-1]:
                nxt.append(i-1)
        else:
            for j in 1, -1:
                if 0 <= i+j < 100001 and not visited[i+j]:
                    nxt.append(i+j)
    
    nxt = list(set(nxt))
    time += 1
    q = []
    for i in nxt:
        if i == 0:
            visited[i] = 1
            continue
        for j in range(i, 100001, i):
            if not visited[j]:
                visited[j] = 1
                q.append(j)
    q = list(set(q))

print(time)
