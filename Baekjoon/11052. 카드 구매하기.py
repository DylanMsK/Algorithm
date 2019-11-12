# url = 'https://www.acmicpc.net/problem/11052'

N = int(input())
ps = [(num, int(price)) for num, price in enumerate(input().split(), 1)]
ps.sort(key=lambda x: (-x[1], -x[0]))
tot = 0
while N:
    for num, price in ps:
        if N-num >= 0:
            N -= num 
            tot += price
            break
print(tot)

