# url = 'https://www.acmicpc.net/problem/17142'

from itertools import combinations
import copy

def get_promiss(arr):
    promiss = []
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                promiss.append((x, y))
    return promiss

def initialize(comb):
    brr = copy.deepcopy(arr)
    # print(comb)
    for y in range(N):
        for x in range(N):
            if brr[y][x] == 2:
                if (x, y) not in comb:
                    brr[y][x] = -1
    return brr

def spread(promiss):
    global brr

    cnt = 0
    for loc in promiss:
        for diff in range(4):
            if 0 <= loc[0]+dx[diff] < N and 0 <= loc[1]+dy[diff] < N and brr[loc[1]+dy[diff]][loc[0]+dx[diff]] in [-1, 0]:
                brr[loc[1]+dy[diff]][loc[0]+dx[diff]] = 2
                cnt += 1
    if cnt:
        return True
    return False

def check():
    for y in range(N):
        for x in range(N):
            if brr[y][x] == 0:
                return False
    return True


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
promiss = get_promiss(arr)
min_ = N*N
dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
for comb in combinations(promiss, M):
    # print(comb)
    brr = initialize(comb)
    time = 0
    while 1:
        # for i in brr:
        #     print(i)
        # print()
        if check():
            break
        promiss = get_promiss(brr)
        sp = spread(promiss)
        time += 1
        if not sp:
            break
            

    if check():
        if time < min_:
            min_ = time
if min_ == N*N:
    print(-1)
else:
    print(min_)

# brr = initialize(((0, 0), (5, 1), (3, 4)))
# t = 0
# while 1:
#     print(t)
#     promiss = get_promiss(brr)
#     sp = spread(promiss)
#     t += 1
#     for i in brr:
#         print(i)
#     if not sp or check():
#         break
# print(t)