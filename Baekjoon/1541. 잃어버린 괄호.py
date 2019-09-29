# url = 'https://www.acmicpc.net/problem/1541'

exps = input().split('-')
result = 0
for i in range(len(exps)):
    sum_ = sum(list(map(int, exps[i].split('+'))))
    if i == 0:
        result += sum_
    else:
        result -= sum_
print(result)
    
