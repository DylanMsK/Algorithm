def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    
    return str(int(''.join(numbers)))


print(solution(['6', '10', '2']))
