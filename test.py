def solution(n):
    if n == 1 or n == 0:
        return 1
    else:
        return solution(n-1) + solution(n-2)

print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))