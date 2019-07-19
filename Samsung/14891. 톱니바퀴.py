# url = 'https://www.acmicpc.net/problem/14891'

gears = []
for _ in range(4):
    gears.append(list(input()))
K = int(input())
cmds = [list(map(int, input().split())) for _ in range(K)]

def rotation(gears, n, d):
    if n < 0 or n >= 8:
        return

    right, left = gears[n][2], gears[n][6]
    if d == 1:
        last = gears[n].pop()
        gears = [last] + gears[n]
    else:
        first = gears.pop(0)
        gears = gears[n].append(first)

    if 0 < n < 7:
        # left
        left_right = gears[n-1][2]
        right_left = gears[n+1][6]
        if left_right == left:
            return
        else:
            rotation(gears, n-1, -d)
        
        if right_left == right:
            return
        else:
            rotation(gears, n+1, -d)
    else:
        return


n, d = cmds.pop(0)
n -= 1
rotation(gears, n, d)
print(gears)

