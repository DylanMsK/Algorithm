# url = 'https://www.acmicpc.net/problem/2164'

N = int(input())
nums = list(range(1, N+1))
if N == 1:
    print(1)
else:
    flag = True
    while len(nums) > 1:
        if flag:
            nxt = [num for idx, num in enumerate(nums) if idx % 2 == 1]
        else:
            nxt = [num for idx, num in enumerate(nums) if idx % 2 == 0]
        if len(nums) % 2 == 0 and len(nxt) % 2:
            flag = False
        elif len(nums) % 2 == 0 and len(nxt) % 2 == 0:
            flag = True
        elif len(nums) % 2 and len(nxt) % 2 == 0:
            flag = False
        else:
            flag = True
        nums = nxt
    print(nums[0])