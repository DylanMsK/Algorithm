# url = 'https://www.acmicpc.net/problem/1932'

N = int(input())
init = [int(input())]
for _ in range(N-1):
    nums = list(map(int, input().split()))
    nums[0] += init[0]
    nums[-1] += init[-1]
    for i in range(1, len(nums)-1):
        nums[i] = max(nums[i]+init[i-1], nums[i]+init[i])
    init = nums
print(max(init))
