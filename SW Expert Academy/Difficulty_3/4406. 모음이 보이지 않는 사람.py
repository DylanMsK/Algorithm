# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcD_66pUEDFAV8&categoryId=AWNcD_66pUEDFAV8&categoryType=CODE'

for tc in range(int(input())):
    string = input()
    result =''
    for s in string:
        if s in ['a', 'e', 'i', 'o', 'u']:
            continue
        result += s
    print(f'#{tc+1} {result}')