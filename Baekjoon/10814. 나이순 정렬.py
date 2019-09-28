# url = 'https://www.acmicpc.net/problem/10814'

N = int(input())
users = [input().split() for _ in range(N)]
users.sort(key=lambda x: int(x[0]))
for i in range(N):
    print(users[i][0], users[i][1])
