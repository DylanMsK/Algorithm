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

# def bfs(lst, tot, inact):
#     global max_

#     for x, y in lst:
#         brr[y][x] = 1

#     nxt = []
#     for x, y in lst:
#         for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
#             nx, ny = x+dx, y+dy
#             if arr[ny][nx] or brr[ny][nx]:
#                 continue
#             brr[ny][nx] = 1
#             nxt.append((nx, ny))

#     if nxt:
#         if isInactives(nxt):
#             bfs(nxt, tot, inact+1)
#         else:
#             bfs(nxt, tot+inact+1, 0)
#     else:
#         max_ = max(max_, tot)
#         return

def isInactives(nxt):
    nums = 0
    for x, y in nxt:
        if (x, y) in promiss:
            nums += 1
    if nums == len(nxt):
        return True
    return False

def check():
    for y in range(1, N+1):
        for x in range(1, N+1):
            if arr[y][x] == 0 and brr[y][x] == 0:
                return False
    return True


# min_ = 1e9
# flag = False
# for comb in combinations(promiss, M):
#     max_ = 0
#     brr = [[0]*(N+2) for _ in range(N+2)]
#     bfs(comb, 0, 0)

#     if check():
#         flag = True
#         min_ = min(min_, max_)

# print(min_) if flag else print(-1)

min_, flag = 1e9, False
for comb in combinations(promiss, M):
    q = comb
    brr = [[0]*(N+2) for _ in range(N+2)]
    tot, inact = 0, 0
    while 1:
        nxt_q = []
        for x, y in q:
            brr[y][x] = 1
            for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
                nx, ny = x+dx, y+dy
                if arr[ny][nx] or brr[ny][nx]:
                    continue
                brr[ny][nx] = 1
                nxt_q.append((nx, ny))
        
        if nxt_q:
            if isInactives(nxt_q):
                inact += 1
            else:
                tot += inact + 1
                inact = 0
                if tot >= min_:
                    break
            q = nxt_q
        else:
            break
    
    if check():
        flag = True
        min_ = min(min_, tot)

print(min_) if flag else print(-1)