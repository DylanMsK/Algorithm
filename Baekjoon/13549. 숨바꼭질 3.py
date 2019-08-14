# url = 'https://www.acmicpc.net/problem/13549'

N, K = map(int,input().split())

visited = [0]*100001
visited[N] = 1
time = 0
q = [N]
while 1:
    if visited[K]:
        break
    nxt = []
    for i in q:
        if i > K:
            if not visited[i-1]:
                nxt.append(i-1)
        else:
            for j in (-1, 1, i):
                if 0 <= i+j <= 100001 and not visited[i+j]:
                    nxt.append(i+j)


