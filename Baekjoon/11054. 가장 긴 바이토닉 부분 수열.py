# url = 'https://www.acmicpc.net/problem/11054'

N = int(input())
nums = list(map(int, input().split()))
init = nums[0]
max_ = 1
length = 1
for i in range(1, N):
    if nums[i] > init:
        length += 1
        init = nums[i]
    else:
        for j in range(i, N):
            if nums[j] < init:
                length += 1
                init = nums[j]
            else:
                max_ = max(max_, length)
                print(max_, nums[j])
                length = 1
                break
print(max_)