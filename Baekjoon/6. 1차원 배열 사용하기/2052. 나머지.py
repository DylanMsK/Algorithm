# url = 'https://www.acmicpc.net/problem/3052'

arr = [0] * 42
for _ in range(10):
    n = int(input())
    left = n % 42
    arr[left] = 1
print(sum(arr))