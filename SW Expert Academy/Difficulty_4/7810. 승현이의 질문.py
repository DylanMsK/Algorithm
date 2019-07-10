# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWslG2zqFQcDFASy'

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_ = max(nums)

    cnts = [0] * (max_+1)
    for i in nums:
        cnts[i] += 1
    
    sum_ = 0
    for i in range(max_, 0, -1):
        sum_ += cnts[i]
        cnts[i] = sum_
        if sum_ >= i:
            break
    
    print(f'#{_+1} {sum_}')
