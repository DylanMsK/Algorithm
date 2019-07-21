# url = 'https://www.acmicpc.net/problem/14891'

gears = []
for _ in range(4):
    gears.append(list(input()))
K = int(input())
cmds = [list(map(int, input().split())) for _ in range(K)]

def rotation(n, d):
    global gears

    if d == 1:
        gears[n] = [gears[n][-1]] + gears[n][:-1]
    else:
        gears[n] = gears[n][1:] + [gears[n][0]]
            
while cmds:
    n, d = cmds.pop(0)
    n -= 1

    right, left = gears[n][2], gears[n][6]
    rotation(n, d)
    for idx, nxt in enumerate(range(n+1, 4)):
        if right != gears[nxt][6]:
            right = gears[nxt][2]
            if idx % 2:
                rotation(nxt, d)
            else:
                rotation(nxt, -d)
        else:
            break

    for idx, nxt in enumerate(range(n-1, -1, -1)):
        if left != gears[nxt][2]:
            left = gears[nxt][6]
            if idx % 2:
                rotation(nxt, d)
            else:
                rotation(nxt, -d)
        else:
            break

tot = [2**i for i in range(4) if gears[i][0] == '1']
print(sum(tot))

