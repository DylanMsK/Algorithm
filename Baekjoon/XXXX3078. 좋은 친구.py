# url = 'https://www.acmicpc.net/problem/3078'

# N, K = map(int, input().split())
# names = {k: [] for k in range(2, 21)}
# for rank in range(N):
#     l = len(input())
#     names[l].append(rank)

# cnt = 0
# for name in names:
#     if not names[name]:
#         continue
#     l = len(names[name])
#     for i in range(l):
#         now = names[name][i]
#         now_idx = i
#         while 1:
#             now_idx -= 1
#             if now_idx < 0:
#                 break
#             if now - names[name][now_idx] <= K:
#                 cnt += 1
#             else:
#                 break
#         now_idx = i
#         while 1:
#             now_idx += 1
#             if now_idx >= l:
#                 break
#             if names[name][now_idx] - now <= K:
#                 cnt += 1
#             else:
#                 break

# print(cnt//2)

# N, K = map(int, input().split())
# s = [0]*N
# for i in range(N):
#     s[i] = len(input())

# cnt = 0
# for i in range(N-K):
#     cnt += s[i+1:i+K+1].count(s[i])
# print(cnt)

import sys
N, K = map(int, sys.stdin.readline().split())
cnt = [0]*21
students = [0]*N
for rank in range(N):
    students[rank] = len(sys.stdin.readline().strip())
    cnt[students[rank]] += students[max(rank-K, 0):min(rank, N)].count(students[rank])
print(sum(cnt))
