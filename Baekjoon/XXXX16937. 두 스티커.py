# url = 'https://www.acmicpc.net/problem/16937'

H, W = map(int, input().split())

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
papers.sort(key=lambda x: x[0]*x[1], reverse=True)
comb = []
for i in range(N-1):
    aa = papers[i][0]*papers[i][1]
    if aa < H*W:
        for j in range(i+1, N):
            bb = papers[j][0]*papers[j][1]
            if aa+bb <= H*W:
                comb.append((aa+bb, papers[i], papers[j]))

comb.sort(key=lambda x: x[0], reverse=True)

flag = 1
for i in comb:
    area, a, b = i
    b.sort()
    # 가로
    if a[0] <= W and a[1] <= H:
        # 오른쪽
        right = [W-a[0], H]
        if b[0]<=min(right) and b[1]<=max(right):
            flag = 0
            break
        # 왼쪽
        bottom = [W, H-a[1]]
        if b[0]<=min(bottom) and b[1]<=max(bottom):
            flag = 0
            break
    # 세로
    elif a[1] <= W and a[0] <= H:
        # 오른쪽
        right = [W-a[1], H]
        if b[0]<=min(right) and b[1]<=max(right):
            flag = 0
            break
        # 왼쪽
        bottom = [W, H-a[0]]
        if b[0]<=min(bottom) and b[1]<=max(bottom):
            flag = 0
            break

if flag:
    print(0)
else:
    print(area)


    # if (a[0]+b[0] <= H and max(a[1], b[1]) <= W) or \
    #    (a[0]+b[1] <= H and max(a[1], b[0]) <= W) or \
    #    (a[1]+b[0] <= H and max(a[0], b[1]) <= W) or \
    #    (a[1]+b[1] <= H and max(a[1], b[1]) <= W):
    #    print(area)
    #    flag = 0
    #    break
    # if (a[0]+b[0] <= W and max(a[1], b[1]) <= H) or \
    #    (a[0]+b[1] <= W and max(a[1], b[0]) <= H) or \
    #    (a[1]+b[0] <= W and max(a[0], b[1]) <= H) or \
    #    (a[1]+b[1] <= W and max(a[1], b[1]) <= H):
    #    print(area)
    #    flag = 0
    #    break

# if flag:
#     print(0)

# arr = [[1]*(W+2)] + [[1]+[0]*W+[1] for _ in range(H)] + [[1]*(W+2)]

# def possible(c):
#     _, (bx, by), (sx, sy) = c
#     if by<=H and bx<=W and not arr[by][bx]:
#         if (sy<=H and bx+sx<=W and not arr[sy][bx+sx]) or (sx<=H and bx+sy<=W and not arr[sx][bx+sy]):
#             return True
#     if bx<=H and by<=W and not arr[bx][by]:
#         if (sx<=H and by+sy<=W and not arr[sx][by+sy]) or (sy<=H and by+sx<=W and not arr[sy][by+sx]):
#             return True
#     return False

# print(comb)
# for c in comb:
#     if possible(c):
#         print(c[0])
#         break
# else:
#     print(0)