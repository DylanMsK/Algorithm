# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQAz7IqAH8DFAWh&categoryId=AWQAz7IqAH8DFAWh&categoryType=CODE'

for tc in range(int(input())):
    string = input()
    flag = True
    for i in range(len(string)//2):
        if string[i] == '*' or string[-(i+1)] == '*':
            break
        if string[i] != string[-(i+1)]:
            flag = False
            break
    if flag:
        res = 'Exist'
    else:
        res = 'Not exist'
    print('#{} {}'.format(tc+1, res))
