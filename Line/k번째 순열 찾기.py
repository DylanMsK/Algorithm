import itertools

nums = input().split()
nums.sort()
k = int(input())

for idx, perm in enumerate(itertools.permutations(nums)):
    if idx == k-1:
        result = ''.join(perm)
        break

print(result)