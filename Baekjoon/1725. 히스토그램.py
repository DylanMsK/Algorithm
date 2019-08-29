# url = 'https://www.acmicpc.net/problem/1725'

N = int(input())
heights = [0]*N
min_ = 1e11
for i in range(N):
    heights[i] = int(input())
    min_ = min(min_, heights[i])

max_area = min_*N
for i in range(N):
    if heights[i] > min_:
        idx = i
        area = 0
        while idx < N:
            if heights[idx] < heights[i]:
                break
            area += heights[i]
            idx += 1
        max_area = max(max_area, area)

print(max_area)