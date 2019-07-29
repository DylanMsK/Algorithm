# url = 'https://www.acmicpc.net/problem/17142'

from itertools import combinations

# N, M = map(int, input().split())
# arr = [[1]*(N+2)]
# for i in range(N):
#     arr.append([1] + list(map(int, input().split())) +[1])
# arr.append([1]*(N+2))

# def check():
#     for y in range(1, N+1):
#         for x in range(1, N+1):
#             if arr[y][x] == 0 and brr[y][x] == 0:
#                 return False
#     return True

# inactive = []
# for y in range(1, N+1):
#     for x in range(1, N+1):
#         if arr[y][x] == 2:
#             inactive.append((x, y))
#             arr[y][x] = 0

# min_ = 1e9
# flag = False
# for comb in combinations(inactive, M):
#     brr = [[0]*(N+2) for _ in range(N+2)]
#     q = list(comb)
#     cnt = 0
#     while 1:
#         nxt_q = []
#         for x, y in q:
#             brr[y][x] = 1
#             for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
#                 nx, ny = x+dx, y+dy
#                 if arr[ny][nx] or brr[ny][nx]:
#                     continue
#                 brr[ny][nx] = 1
#                 nxt_q.append((nx, ny))
#         if nxt_q:
#             for x, y in nxt_q:
#                 if (x, y) in inactive:
#                     continue
#                 else:
#                     cnt += 1
#                     break
#             if cnt >= min_:
#                 break
#             q = nxt_q
#         else:
#             break

#     if check():
#         flag = True
#         min_ = min(min_, cnt)

# print(min_) if flag else print(-1)

N, M = map(int, input().split())
arr = [[1]*(N+2)]
for _ in range(N):
    arr.append([1] + list(map(int, input().split())) + [1])
arr.append([1]*(N+2))

promiss = []
for y in range(1, N+1):
    for x in range(1, N+1):
        if arr[y][x] == 2:
            promiss.append((x, y))
            arr[y][x] = 0

def dfs(lst, cnt):
    global max_

    if arr[y][x] or brr[y][x]:
        max_ = max(max_, cnt)
        return
    else:
        brr[y][x] = 1
        dfs(x, y-1, cnt+1)
        dfs(x+1, y, cnt+1)
        dfs(x, y+1, cnt+1)
        dfs(x-1, y, cnt+1)




def check():
    for y in range(1, N+1):
        for x in range(1, N+1):
            if arr[y][x] == 0 and brr[y][x] == 0:
                return False
    return True


min_ = 1e9
flag = False
for comb in combinations(promiss, M):
    max_ = 0
    brr = [[0]*(N+2) for _ in range(N+2)]
    for x, y in comb:
        print(x, y)
        dfs(x, y, 0)
    if check():
        flag = True
        min_ = min(min_, max_)
    print()
    print(comb)
    print(max_)
    for i in brr:
        print(i)
    break

print(min_) if flag else print(-1)