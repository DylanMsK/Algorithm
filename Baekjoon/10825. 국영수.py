# url = 'https://www.acmicpc.net/problem/10825'

N = int(input())
students = [input().split() for _ in range(N)]
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for stu in students:
    print(stu[0])