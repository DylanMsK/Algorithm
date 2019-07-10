# url = 'https://www.acmicpc.net/problem/14501'

# N = int(input())
# table =[list(map(int, input().split())) for _ in range(N)]
# max_ = 0

# def func(day, pay):
#     global max_
#     if day >= N:
#         if day == N:
#             tot = sum(pay)
#         else:
#             tot = sum(pay[:-1])

#         if tot > max_:
#             max_ = tot
#         return

#     # 해당 날짜에 상담 X
#     func(day+1, pay)

#     # 해당 날짜에 상담 O
#     nday, npay = day+table[day][0], pay+[table[day][1]]
#     func(nday, npay)

# func(0, [])
# print(max_)

N = int(input())
info = list(list(map(int, input().split())) for _ in range(N))
dp = list(0 for _ in range(N))


for i in range(N):
    if i + info[i][0] <= N:
        dp[i] = info[i][1]
        for j in range(i):
            if j + info[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + info[i][1])

print(max(dp))