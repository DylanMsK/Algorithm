# url = 'https://www.acmicpc.net/problem/2312'

tc = int(input())
for _ in range(tc):
    N = int(input())
    args = {}
    while N > 1:
        for i in range(2, N+1):
            if N % i == 0:
                N //= i
                if args.get(i):
                    args[i] += 1
                else:
                    args[i] = 1
                break
    for i, j in args.items():
        print(i, j)
 