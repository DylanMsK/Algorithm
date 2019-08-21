# url = 'https://www.acmicpc.net/problem/16925'

N = int(input())
data = [input() for _ in range(2*N-2)]
r = []
for i in range(2*N-2):
    l = len(data[i])
    if l == N-1:
        r.append(data[i])
    data[i] = (l, data[i])
s = []
if r[0][1:] == r[1][:-1]:
    s.append(r[0]+r[1][-1])
if r[0][:-1] == r[1][1:]:
    s.append(r[1]+r[0][-1])

def find(s):
    prefix, suffix = [1]*(N-1), [1]*(N-1)
    res = ''
    for i in data:
        if prefix[i[0]-1] and i[1] == s[:i[0]]:
            res += 'P'
            prefix[i[0]-1] = 0
            continue
        if suffix[-i[0]] and i[1] == s[-i[0]:]:
            res += 'S'
            suffix[-i[0]] = 0
            continue
        return False
    return res

for i in s:
    res = find(i)
    if res:
        print(i)
        print(res)
        break