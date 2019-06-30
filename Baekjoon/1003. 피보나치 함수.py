# url = 'https://www.acmicpc.net/problem/1003'


tc = int(input())
for _ in range(tc):
    n = int(input())
    nums = [(1, 0), (0, 1)]
    for i in range(2, n+1):
        nums.append((nums[i-1][0] + nums[i-2][0], nums[i-1][1] + nums[i-2][1]))
    print(f'{nums[n][0]} {nums[n][1]}')

