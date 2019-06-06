# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWZ2IErKCwUDFAUQ&categoryId=AWZ2IErKCwUDFAUQ&categoryType=CODE'
import itertools

N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    results = []
    for i in itertools.combinations(nums, 3):
        sum_ = sum(i)
        if sum_ not in results:
            results.append(sum(i))
    results.sort()
    print(f'#{_+1} {results[-5]}')


