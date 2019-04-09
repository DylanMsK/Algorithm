# url = 'https://www.acmicpc.net/problem/17136' 
import copy

def find(x, y, k):
    global arr
    if arr[y][x] and sum(arr[y][x:x+k]) == k:
        flag = True
        for row in range(1, k):
            if sum(arr[y+row][x:x+k]) != k:
                flag = False
                break
        if flag:
            return True
    return False



def backtrack(arr, cnt, remain):
    global arr
    if cnt > min_:
        return

    for k in range(5, 0, -1):
        for y in range(10):
            for x in range(10):
                prob = find(x, y, k)
                if prob:
                    brr = copy.deepcopy(arr)
                    backtrack

    


arr = [list(map(int, input().split())) for _ in range(10)]

min_ = 30
backtrack(arr, 0, [5, 5, 5, 5, 5])

