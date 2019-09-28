# url = 'https://www.acmicpc.net/problem/11651'



N = int(input())
locations = [tuple(map(int, input().split())) for _ in range(N)]
locations.sort(key=lambda x: (x[1], x[0]))
for i in locations:
    print(i[0], i[1])