# url = 'https://www.acmicpc.net/problem/17406'
from itertools import permutations
from copy import deepcopy


N, M, K = map(int, input().split())
brr = [list(map(int, input().split())) for _ in range(N)]
cmd = [list(map(int, input().split())) for _ in range(K)]

def top(x, y, cnt):
    x, y = x-cnt, y-cnt
    length = cnt*2+1
    nxt = arr[y][x:x+length]
    change = [0] + nxt[:-1]
    for nx in range(x, x+length):
        arr[y][nx] = change[nx+1-length]
    return nxt[-1]

def right(x, y, cnt, pass_):
    x, y = x+cnt, y-cnt
    length = cnt*2+1
    print(x, y, length)
    nxt = [arr[ny][x] for ny in range(y, y+length)]
    nxt[0] = pass_
    change = nxt[:-1]
    for idx, ny in enumerate(range(y+1, y+length)):
        arr[ny][x] = change[idx]
    return nxt[-1]

def bottom(x, y, cnt, pass_):
    x, y = x-cnt, y+cnt
    length = cnt*2+1
    nxt = arr[y][x:x+length][::-1]
    nxt[0] = pass_
    change = nxt[:-1]
    for idx, nx in enumerate(range(x+cnt-1, x-cnt-1, -1)):
        arr[y][nx] = change[idx]
    return nxt[-1]

def left(x, y, cnt, pass_):
    x, y = x-cnt, y+cnt
    length = cnt*2+1
    nxt = [arr[ny][x] for ny in range(y-1, y-length, -1)][::-1]
    nxt[0] = pass_
    for idx, ny in enumerate(range(y-1, y-length, -1)):
        arr[ny][x] = nxt[idx]

def cal_min():
    global min_

    for i in arr:
        min_ = min(sum(i), min_)
        

min_ = 1e10
for per in permutations(cmd):
    arr = deepcopy(brr)
    for p in per:
        r, c, s = p
        r, c = r-1, c-1
        print((r, c, s))
        for cnt in range(1, s+1):
            pass_ = top(r, c, cnt)
            pass_ = right(r, c, cnt, pass_)
            pass_ = bottom(r, c, cnt, pass_)
            left(r, c, cnt, pass_)
    cal_min()

print(min_)
