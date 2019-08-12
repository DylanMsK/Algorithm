# url = 'https://www.acmicpc.net/problem/12851'

N, K = map(int, input().split())

time = 0
visited = [0] * (100001)
visited[N] = 1
present = [N]
while 1:
    nxt = []
    # print(time, present, visited)
    cnt = [0] * 100001
    for now in present:
        cnt[now] = 1
        for j in (-1, 1, now):
            if 0 <= now+j <= 100000:
                visited[now+j] += cnt[now]
                if now+j not in nxt:
                    nxt.append(now+j)
    time += 1
    if K in nxt:
        # print(time, nxt, cnt)
        break
    present = nxt

print(time)
print(visited[K])