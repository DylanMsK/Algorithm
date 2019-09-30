# url = 'https://www.acmicpc.net/problem/3009'
x, y = [], []
for _ in range(3):
    a, b = map(int, input().split())
    if a in x:
        x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)
print(x[0], y[0])
