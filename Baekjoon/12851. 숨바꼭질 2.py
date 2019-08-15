# url = 'https://www.acmicpc.net/problem/12851'

N, K = map(int, input().split())

time = 0
visited = [0] * 100001
cnt = [0] * 100001
q = [N]
visited[N] = 1
cnt[N] = 1
while 1:
    if visited[K]:
        break
        
    nxt = []
    for i in q:
        if i > K:
            if not visited[i-1]:
                nxt.append(i-1)
                cnt[i-1] += cnt[i]
        else:
            for j in (-1, 1, i):
                if 0 <= i+j <= 100001 and not visited[i+j]:
                    nxt.append(i+j)
                    cnt[i+j] += cnt[i]

    time += 1
    nxt = list(set(nxt))

    for i in nxt:
        visited[i] = 1

    q = nxt

print(time)
print(cnt[K])