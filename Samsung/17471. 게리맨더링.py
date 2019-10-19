# url = 'https://www.acmicpc.net/problem/17471'
from itertools import combinations

N = int(input())
nums = list(map(int, input().split()))
connected = {i: list(map(int, input().split()))[1:] for i in range(N)}

def is_connected(comb):
    q = []
    for c in comb:
        q += connected[c]
    q = [i-1 for i in set(q)]
    # print(set(q))
    # print(set(comb))
    # print(set(q) & set(comb))
    if set(q) & set(comb) == set(comb):
        print(comb)
        return True
    return False

def diff(a, b):
    sum_a = sum([nums[i] for i in a])
    sum_b = sum([nums[i] for i in b])
    return abs(sum_a - sum_b)

min_ = 1e10
for k in range(1, N//2+1):
    for comb in combinations(list(range(N)), k):
        cities = set(range(N))
        a = set(comb)
        b = cities - a
        if is_connected(a) and is_connected(b):
            # print(a, b)
            min_ = min(min_, diff(a, b))

# print(is_connected((1, 4, 5)))

if min_ == 1e10:
    print(-1)
else:
    print(min_)