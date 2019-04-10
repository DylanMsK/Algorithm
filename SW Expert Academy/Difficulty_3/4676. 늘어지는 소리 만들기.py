# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWRKWITqfvIDFAV8&categoryId=AWRKWITqfvIDFAV8&categoryType=CODE'

for tc in range(int(input())):
    string = input()
    N = int(input())
    init = list(map(int,input().split()))
    hipen = {}
    for i in init:
        if i in hipen:
            hipen[i] += 1
        else:
            hipen[i] = 1
    
    result = ''
    for i in range(len(string)+1):
        if i in hipen:
            result += '-' * hipen[i]
        if i < len(string):
            result += string[i]

    print('#{} {}'.format(tc+1, result))