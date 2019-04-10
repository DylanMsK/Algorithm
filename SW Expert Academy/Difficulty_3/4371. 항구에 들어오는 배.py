# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMedCxalW8DFAXd&categoryId=AWMedCxalW8DFAXd&categoryType=CODE'

for tc in range(int(input())):
    N = int(input())
    lst = list(int(input()) for _ in range(N))
    for i in range(1, N):
        lst[i] = lst[i] - 1

    cnt = 0
    diff = lst[1:]
    while diff:
        cnt += 1
        min_ = diff.pop(diff.index(min(diff)))
        diff = [i for i in diff if i % min_]
    print(f'#{tc+1} {cnt}')