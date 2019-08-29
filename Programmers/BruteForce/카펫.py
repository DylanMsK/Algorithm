
def solution(brown, red):
    answer = []
    for i in range(int(red**0.5)+1, 1, -1):
        if red % i == 0:
            print(i, red//i)
            if (i*2) + ((red // i)*2) == brown-4:
                answer = [i+2, (red // i)+2]
                break
    return answer

print(solution(8, 1))