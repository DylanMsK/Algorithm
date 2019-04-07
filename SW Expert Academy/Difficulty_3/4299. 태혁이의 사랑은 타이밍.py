# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWLv6mx6htoDFAVV&categoryId=AWLv6mx6htoDFAVV&categoryType=CODE'
for tc in range(int(input())):
    D, H, M = map(int, input().split())
    you = D * 24 * 60 + H * 60 + M
    base = 11 * 24 * 60 + 11 * 60 + 11
    if you - base >= 0:
        minutes = you - base
    else:
        minutes = -1
    print(f'#{tc+1} {minutes}')