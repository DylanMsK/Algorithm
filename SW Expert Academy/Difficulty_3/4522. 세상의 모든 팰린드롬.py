# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWO6Oao6N4QDFAWw&categoryId=AWO6Oao6N4QDFAWw&categoryType=CODE'

for tc in range(int(input())):
    string = input()
    flag = True
    for i in range(len(string)//2):
        if string[i] == '?':
            continue
        if string[i] != string[-(i+1)]:
            if string[-(i+1)] == '?':
                continue
            flag = False
            break
    if flag:
        res = 'Exist'
    else:
        res = 'Not exist'
    print(f'#{tc+1} {res}')