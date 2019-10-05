# url = 'https://www.acmicpc.net/problem/10773'

K = int(input())
lst = []
for _ in range(K):
    money = int(input())
    if money:
        lst.append(money)
    else:
        lst.pop()
print(sum(lst))