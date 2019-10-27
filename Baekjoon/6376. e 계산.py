# url = 'https://www.acmicpc.net/problem/6376'

def e(n):
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n+1):
            fact = 1
            for j in range(1, i+1):
                fact *= j
            res += 1/fact
        return res

text = """n e
- -----------
0 1
1 2
2 2.5
3 2.666666667
4 2.708333333"""
print(text)
for i in range(5, 10):
    print('%d %.9f' % (i, e(i)))