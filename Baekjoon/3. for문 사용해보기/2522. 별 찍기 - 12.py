# url = 'https://www.acmicpc.net/problem/2522'

N = int(input())
init = 1
for i in range(1, 2*N):
    print(' '*(N-init) + '*'*(init))
    if i >= N:
        init -= 1
    else:
        init += 1