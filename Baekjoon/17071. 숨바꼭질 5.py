# url = 'https://www.acmicpc.net/problem/17071'

N, K = map(int, input().split())
time = 0
if N == K:
    print(time)
else:
    l = 500001
    # odd, even = [0]*l, [0]*l
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
        if visited[K]:
            break
        q = list(set(nxt))

    print(time) if K < l else print(-1)