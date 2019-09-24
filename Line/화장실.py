n = int(input())
students = [tuple(map(int, input().split())) for _ in range(n)]
students.sort(key=lambda x: x[0])

max_ = 1
for i in range(n-1):
    cnt = 1
    for j in range(i+1, n):
        if students[i][0] <= students[j][0] < students[i][1]:
            cnt += 1
        else:
            break
    max_ = max(max_, cnt)

print(max_)