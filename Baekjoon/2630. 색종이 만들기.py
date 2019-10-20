# url = 'https://www.acmicpc.net/problem/2630'


def devide(x, y, t):
    global blue, white

    type = arr[y][x]
    flag = True
    for i in range(y, y+t):
        if not flag:
            break
        for j in range(x, x+t):
            if type != arr[i][j]:
                flag = False
                devide(x, y, t//2)
                devide(x+t//2, y, t//2)
                devide(x, y+t//2, t//2)
                devide(x+t//2, y+t//2, t//2)
                break
    if flag:
        if type == 0:
            white += 1
        else:
            blue += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
blue, white = 0, 0
devide(0, 0, N)
print(white)
print(blue)
