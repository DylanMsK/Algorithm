# url = 'https://www.acmicpc.net/problem/1676'

N = int(input())
num = 1
if N >= 1:
    for i in range(1, N+1):
        num *= i
        
cnt = 0
for i in str(num)[::-1]:
    if i != '0':
        break
    cnt += 1

print(cnt)


