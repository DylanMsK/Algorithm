# url = 'https://www.acmicpc.net/problem/17143'

R, C, M = map(int, input().split())
mat = [[0]*C for r in range(R)]
sharks = []
for _ in range(M):
    shark = list(map(int, input().split()))
    mat[y-1][x-1] = shark

answer = 0
for col in range(1, M):
    # fishing shark
    for i in range(R):
        if mat[col][i]:
            shark = mat[col][i]
            sharks.remove(shark)
            answer += shark[-1]
            mat[col][i] = 0
            break
    
    # moving shark
    while sharks:
        r, c, s, d, z = sharks.pop(0)
        nr, nc, ns = r, c, s
        while ns > 0:
            ns -= 1
            if d == 1:
                if nr == 1:
                    nr += 1
                    d = 2
                else:
                    nr -= 1
            elif d == 2:
                if nr == R:
                    nr -= 1
                    d = 1
                else:
                    nr += 1
            elif d == 3:
                if nc == C:
                    nc -= 1
                    d = 4
                else:
                    nc += 1
            else:
                if nc == 1:
                    nc += 1
                    d = 3
                else:
                    nc -= 1