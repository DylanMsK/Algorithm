# url = 'https://www.acmicpc.net/problem/11650'

N = int(input())
locations = [tuple(map(int, input().split())) for _ in range(N)]
locations.sort(key=lambda x: (x[0], x[1]))
for i in locations:
    print(i[0], i[1])