# url = 'https://www.acmicpc.net/problem/1987'


def dfs(x, y, string):
    global arr, max_
    string += arr[y][x]

    for i in range(4):
        if 0 <= x + dx[i] < C and 0 <= y +dy[i] < R and arr[y+dy[i]][x+dx[i]] not in string:
            string += arr[y+dy[i]][x+dx[i]]
            dfs(x+dx[i], y+dy[i], string)
            string = string[:-1]
    else:
        if len(string) > max_:
            max_ = len(string)
            print(string)
        return


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
max_ = 0
dfs(0, 0, '')
print(max_)