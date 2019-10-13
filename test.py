def solution(m, n, puddles):
    arr = [[0]*(m) for _ in range(n)]
    arr[0][0] = 1
    for x, y in puddles:
        arr[y-1][x-1] = -1
        
    for y in range(n):
        for x in range(m):
            if arr[y][x] == -1:
                continue
            else:
                if y > 0 and arr[y-1][x] != -1:
                    arr[y][x] += arr[y-1][x]
                if x > 0 and arr[y][x-1] != -1:
                    arr[y][x] += arr[y][x-1]
    for i in arr:
        print(i)
    return arr[n-1][m-1]

solution(4, 3, [[2, 2]])