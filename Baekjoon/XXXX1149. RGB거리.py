# url = 'https://www.acmicpc.net/problem/1149'

N = int(input())
r, g, b = list(map(int, input().split()))
price = []

for _ in range(1, N):
    r, g, b = map(int, input().split())
    nxt = []

