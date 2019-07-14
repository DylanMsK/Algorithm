# url = 'https://www.acmicpc.net/problem/1037'

N = int(input())
factors = list(map(int, input().split()))
print(min(factors) * max(factors))