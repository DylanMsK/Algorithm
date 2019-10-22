# url = 'https://www.acmicpc.net/problem/15953'

first = [0]*101
second = [0]*65
for i in range(101):
    if i == 0:
        continue
    elif i < 2:
        first[i] = 500
    elif i < 4:
        first[i] = 300
    elif i < 7:
        first[i] = 200
    elif i < 11:
        first[i] = 50
    elif i < 16:
        first[i] = 30
    elif i < 22:
        first[i] = 10
    else:
        break

for i in range(65):
    if i == 0:
        continue
    elif i < 2:
        second[i] = 512
    elif i < 4:
        second[i] = 256
    elif i < 8:
        second[i] = 128
    elif i < 16:
        second[i] = 64
    elif i < 32:
        second[i] = 32
    else:
        break

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print((first[a] + second[b])*10000)