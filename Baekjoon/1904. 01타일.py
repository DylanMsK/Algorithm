# url = 'https://www.acmicpc.net/problem/1904'

N = int(input())
if N == 1:
    print(1)
else:
    a, b = 1, 2
    for i in range(N-2):
        a, b = b, a+b
    print(b % 15746)