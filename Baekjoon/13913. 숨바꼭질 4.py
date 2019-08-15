# url = 'https://www.acmicpc.net/problem/13913'

N, K = map(int, input().split())
if N >= K:
    print(N-K)
    for i in range(N, K-1, -1):
        print(i, end=" ")
else:
    length = max(100001, max(N, K)*2)
    visited, path = [0]*length, ['']*length
    visited[N], path[N] = 1, str(N)
    q = [N]
    time = 0
    while 1:
        if visited[K]:
            break
        nq = []
        for i in q:
            if i > K:
                if 0 <= i+j < length and not visited[i+j]:
                    path[i-1] = path[i]+' '+str(i-1)
                    nq.append(i+j)
            for j in i, 1, -1:
                if 0 <= i+j < length and not visited[i+j]:
                    path[i+j] = path[i]+' '+str(i+j)
                    nq.append(i+j)
            path[i] = ''

        nq = list(set(nq))
        time += 1
        for i in nq:
            visited[i] = 1
            
        q = nq

    print(time)
    print(path[K])