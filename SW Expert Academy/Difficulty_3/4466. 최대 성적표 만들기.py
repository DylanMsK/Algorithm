# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWOUfCJ6qVMDFAWg&categoryId=AWOUfCJ6qVMDFAWg&categoryType=CODE'
for tc in range(int(input())):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort()
    print(f'#{tc+1} {sum(scores[-K:])}')