# url = 'https://www.acmicpc.net/problem/1463'

from heapq import heappop, heappush

x = int(input())

cnt = 0
q = [(0, x)]
while q:
    cnt, num = heappop(q)
    
    if num == 1:
        break
    if num < 1:
        continue

    cnt += 1
    if num % 3 == 0:
        heappush(q, (cnt, num//3))
    if num % 2 == 0:
        heappush(q, (cnt, num//2))
    heappush(q, (cnt, num-1))

print(cnt)