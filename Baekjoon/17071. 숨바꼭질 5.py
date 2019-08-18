# url = 'https://www.acmicpc.net/problem/17071'

N, K = map(int, input().split())
time = 0
if N == K:
    print(time)
else:
    l = 500001
    visited = [0]*l
    visited[N] = 1
    q = [N]
    while 1:
        time += 1
        K += time
        if K >= l:
            break
        nxt = []
        for i in q:
            for j in i, 1, -1:
                if 0 <= i+j < l:
                    nxt.append(i+j)
                    visited[i+j] = 1
        q = list(set(nxt))
        if K in q:
            break
    print(time) if K < l else print(-1)
