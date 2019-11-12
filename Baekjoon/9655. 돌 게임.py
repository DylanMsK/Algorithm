# url = 'https://www.acmicpc.net/problem/9655'

N = int(input())
turn, left = N // 3, N % 3
if turn == 0:
    print(['', 'SK', 'CY'][left])
elif turn % 2:
    print(['SK', 'CY', 'SK'][left])
else:
    print(['CY', 'SK', 'CY'][left])