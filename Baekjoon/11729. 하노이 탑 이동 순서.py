# url = 'https://www.acmicpc.net/problem/11729'


def hanoi(num, _from, _by, _to):
    if num == 1:
        res.append((_from, _to))
        return
    else:
        hanoi(num-1, _from, _to, _by)
        res.append((_from, _to))
        hanoi(num-1, _by, _from, _to)


N = int(input())
res = []
hanoi(N, 1, 2, 3)
print(len(res))
for i, j in res:
    print(i, j)