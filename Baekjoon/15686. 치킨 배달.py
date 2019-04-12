# url = 'https://www.acmicpc.net/problem/15686'
import sys
from itertools import combinations
# sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
houses = []
for y in range(N):
    for x in range(N):
        if city[y][x]:
            if city[y][x] == 1:
                houses.append((x, y))
            else:
                chicken.append((x, y))

min_ = 4 * N * N
for combi in combinations(chicken, M):
    sum_ = 0
    for house in houses:
        min_chick = 4 * N * N
        for chick in combi:
            distance = abs(house[0]-chick[0]) + abs(house[1]-chick[1])
            if distance < min_chick:
                min_chick = distance
        sum_ += min_chick
    if sum_ < min_:
        min_ = sum_

print(min_)