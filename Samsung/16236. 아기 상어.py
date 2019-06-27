# url = 'https://www.acmicpc.net/problem/16236'

def find_fishes(arr, ):
    for 

N = int(input())
arr = [list(map(int, input().split()))]

fishes = []
for y in range(N):
    for x in range(N):
        if arr[y][x]:
            if arr[y][x] == '9':
                shark = [x, y]
            elif arr[y][x] == '1':
                fishes.append([x, y])
            else:
                continue

arr.sort(key=lambda fish: fish[0])