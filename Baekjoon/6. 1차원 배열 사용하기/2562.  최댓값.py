# url = 'https://www.acmicpc.net/problem/2562'

max_, idx = 0, 0

for _ in range(9):
    n = int(input())
    if n > max_:
        max_, idx = n, _+1

print(f'{max_}\n{idx}')