# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14zIwqAHwCFAYD&categoryId=AV14zIwqAHwCFAYD&categoryType=CODE'

import sys
sys.stdin = open('/Users/dylan/Desktop/github/TIL/Algorithm/SW Expert Academy/Difficulty_3/input.txt', 'r')

def insert(lst, x, y, s):
    lst = lst[:x] + s + lst[x:]
    return lst

def delete(lst, x, y):
    lst = lst[:x] + lst[x+y:]
    return lst

def add(lst, y, s):
    lst = lst + s
    return lst

for _ in range(10):
    N = int(input())
    lst = list(map(int, input().split()))
    num_cmd = int(input())
    cmd = input().split()
    idx = 0
    while  idx < len(cmd):
        if cmd[idx] == 'I':
            x = int(cmd[idx+1])
            y = int(cmd[idx+2])
            s = cmd[idx+3:idx+3+y]
            lst = insert(lst, x, y, s)
            idx += 3 + y

        elif cmd[idx] == 'D':
            x = int(cmd[idx+1])
            y = int(cmd[idx+2])
            lst = delete(lst, x, y)
            idx += 3

        elif cmd[idx] == 'A':
            y = int(cmd[idx+1])
            s = cmd[idx+2:idx+2+y]
            lst = add(lst, y, s)
            idx += 2 + y
    
    print(f'#{_+1} {" ".join([i for i in lst[:10]])}')