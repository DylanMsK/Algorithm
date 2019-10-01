# url = 'https://www.acmicpc.net/problem/3036'

N = int(input())
init, *lefty = map(int, input().split())
for i in lefty:
    for gcf in range(i, 0, -1):
        if init % gcf == 0 and i % gcf == 0:
            print(f'{init//gcf}/{i//gcf}')
            break