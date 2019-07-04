# url = 'https://www.acmicpc.net/problem/1850'

a, b = map(int, input().split())
m = min(min(a, b), abs(a-b))
com = [1]
nums = [0] + [1]*m
for i in range(2, int(m**0.5)):
    if nums[i]:
        com.append(i)
        for j in range(i+i, m+1, i):
            nums[j] = 0
            com.append(j)
com.append(m)
com.sort(reverse=True)
for i in com:
    if a % i == 0 and b % i == 0:
        m = i
        break

print('1'*m)