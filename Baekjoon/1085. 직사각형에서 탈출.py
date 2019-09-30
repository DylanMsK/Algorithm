# url = 'https://www.acmicpc.net/problem/1085'

x, y, w, h = map(int, input().split())
print(min(h-y, w-x, x, y))