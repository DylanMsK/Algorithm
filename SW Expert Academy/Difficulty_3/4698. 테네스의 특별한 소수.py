# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWRuoqCKkE0DFAXt&categoryId=AWRuoqCKkE0DFAXt&categoryType=CODE'


nums = [i for i in range(1000001)]
nums[1] = 0
for i in range(int(1000001**0.5)):
    if nums[i] == 0:
        continue
    for j in range(i+i, 1000001, i):
        nums[j] = 0

primes = [i for i in nums if i]
for tc in range(int(input())):
    D, A, B = map(int, input().split())
    d = str(D)
    cnt = 0
    for i in primes:
        if A <= i <= B:
            if d in str(i):
                cnt += 1
        if i > B:
            break
    print('#{} {}'.format(tc+1, cnt))