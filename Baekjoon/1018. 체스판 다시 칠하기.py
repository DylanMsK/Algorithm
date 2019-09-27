# url = 'https://www.acmicpc.net/problem/1018'

N, M = map(int, input().split())
board = [input() for _ in range(N)]
w, b = 'WBWBWBWB', 'BWBWBWBW'
white = [w, b] * 4
black = [b, w] * 4

min_ = 64
for y in range(N-7):
    for x in range(M-7):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if board[y+i][x+j] != white[i][j]:
                    cnt += 1
            if cnt > min_:
                break
        min_ = min(min_, cnt)
        cnt = 0
        for i in range(8):
            for j in range(8):
                if board[y+i][x+j] != black[i][j]:
                    cnt += 1
            if cnt > min_:
                break
        min_ = min(min_, cnt)

print(min_)
