# url = 'https://www.acmicpc.net/problem/14501'

N = int(input())
table =[[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
max_ = 0

def func(day, pay):
    global max_
    if day > N:
        if day == N+1:
            tot = sum(pay)
        else:
            tot = sum(pay[:-1])

        if tot > max_:
            max_ = tot
        return

    # 해당 날짜에 상담 X
    func(day+1, pay)

    # 해당 날짜에 상담 O
    nday, npay = day+table[day][0], pay+[table[day][1]]

    func(nday, npay)

func(1, [])
print(max_)
