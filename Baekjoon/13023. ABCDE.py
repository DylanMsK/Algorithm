# url = 'https://www.acmicpc.net/problem/13023'

N, M = map(int, input().split())
relation = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

def dfs(cnt, nxt):
    global flag
    
    visited[nxt] = True
    if cnt == 4:
        flag = True
        return

    for i in relation[nxt]:
        if not visited[i]:
            dfs(cnt+1, i)
            visited[i] = False


flag = False
for r in range(N):
    dfs(0, r)
    visited[r] = False
    if flag:
        print(1)
        break

else:
    print(0)