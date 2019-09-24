n, m = map(int, input().strip().split())
x, y = map(int, input().strip().split())

if not 0 <= x <= n or not 0 <= y <= m:
    print('fail')
else:
    time = x+y
    case = 1
    for i in range(1, x+y+1):
        case *= i
    for i in range(1, x+1):
        case //= i
    for i in range(1, y+1):
        case //= i
    print(time)
    print(case)