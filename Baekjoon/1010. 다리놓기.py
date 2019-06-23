# url = 'https://www.acmicpc.net/problem/1010'

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    k = (M-N)+1
    tot = 0
    while k > 0:
        for i in range(k, 0, -1):
            tot += i
        k -= 1

    print(tot)