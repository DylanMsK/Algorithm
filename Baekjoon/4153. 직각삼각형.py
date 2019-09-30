# url = 'https://www.acmicpc.net/problem/4153'

while 1:
    nums = list(map(int, input().split()))
    if sum(nums):
        nums.sort()
        if nums[2]**2 == nums[1]**2 + nums[0]**2:
            print('right')
        else:
            print('wrong')
    else:
        break