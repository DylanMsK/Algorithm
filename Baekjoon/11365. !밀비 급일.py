# url = 'https://www.acmicpc.net/problem/11365'

while 1:
    string = input()
    if string == 'END':
        break
    for i in range(len(string)-1, -1, -1):
        print(string[i], end='')
    print()