# url = 'https://www.acmicpc.net/problem/3190'



N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
cmd = [input().split() for _ in range(L)]

directions = {
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
    'N': (-1, 0)
}
rotation = {
    'E': {'L': 'N', 'D': 'S'},
    'S': {'L': 'E', 'D': 'W'},
    'W': {'L': 'S', 'D': 'N'},
    'N': {'L': 'W', 'D': 'E'},
}
# print(apples)
cnt = 0
snake = [(0, 0)]
d = 'E'
while 1:

    if cmd and cnt == int(cmd[0][0]):
        _, curve = cmd.pop(0)
        d = rotation[d][curve]
    cnt += 1

    y, x = snake[0]
    ny, nx = y+directions[d][0], x+directions[d][1]
    if (ny+1, nx+1) in apples:
        # print('사과 먹음')
        apples.pop(apples.index((ny+1, nx+1)))
    else:
        if (ny, nx) in snake[1:]:
            break
        snake = snake[:-1]
    # 보드를 벗어났을때
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        # print('보드 벗어남')
        break
    # 몸에 부딪을쳤을때    
    if (ny, nx) in snake:
        # print('먹어버림')
        break
    snake  = [(ny, nx)] + snake
    # print(f'{cnt}초 {snake}')


print(cnt)