# url = 'https://www.acmicpc.net/problem/1015'

N = int(input())
A = list(map(int, input().split()))

P = [-1] * N
idx = 0
for i in range(N):
    min_idx = A.index(min(A))
    A[min_idx] = 1001
    P[min_idx] = idx
    idx += 1
print(' '.join([str(i) for i in P]))
