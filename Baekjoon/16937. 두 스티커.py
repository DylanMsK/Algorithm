# url = 'https://www.acmicpc.net/problem/16937'

H, W = map(int, input().split())

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
papers.sort(key=lambda x: x[0]*x[1], reverse=True)
comb = []
for i in range(N-1):
    a = papers[i]
    for j in range(i+1, N):
        b = papers[j]
        area = a[0]*a[1]+b[0]*b[1]
        if area <= H*W:
            comb.append((area, a, b))

comb.sort(key=lambda x: x[0], reverse=True)
arr = [[1]*(W+2)] + [[1]+[0]*W+[1] for _ in range(H)] + [[1]*(W+2)]

# for i in arr:
#     print(i)

def possible(c):
    _, (bx, by), (sx, sy) = c
    if by<=H and bx<=W and not arr[by][bx]:
        if (sy<=H and bx+sx<=W and not arr[sy][bx+sx]) or (sx<=H and bx+sy<=W and not arr[sx][bx+sy]):
            return True
    if bx<=H and by<=W and not arr[bx][by]:
        if (sx<=H and by+sy<=W and not arr[sx][by+sy]) or (sy<=H and by+sx<=W and not arr[sy][by+sx]):
            return True
    return False

for c in comb:
    if possible(c):
        print(c[0])
        break
else:
    print(0)