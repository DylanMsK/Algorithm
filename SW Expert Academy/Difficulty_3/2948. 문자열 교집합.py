# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-Un3G64SUDFAXr&categoryId=AV-Un3G64SUDFAXr&categoryType=CODE'

for tc in range(int(input())):
    N, M = map(int, input().split())
    lst1 = set(input().split())
    lst2 = set(input().split())
    result = lst1.intersection(lst2)
    print('#{} {}'.format(tc+1, len(result)))