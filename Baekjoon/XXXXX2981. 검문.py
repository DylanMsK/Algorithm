# url = 'https://www.acmicpc.net/problem/2981'

N = int(input())
min_ = 1e9
nums = []
for _ in range(N):
    x = int(input())
    min_ = min(x, min_)
    nums.append(x)
nums.pop(nums.index(min_))

max_com = 0
for i in range(min_, 1, -1):
    for num in nums:
        if num % i:
            break
    else:
        max_com = i
        break

for i in range(max_com, min_+1, max_com):
    left = min_ % i
    for num in nums:
        if num % i != left:
            break
    else:
        print(i, end=" ")