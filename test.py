def solution(N):
    # write your code in Python 3.6
    binary = ''
    while N > 1:
        if N % 2:
            binary += '1'
        else:
            binary += '0'
        N //= 2
    binary += '1'
    binary = binary[::-1]
    max_, cnt = 0, 0
    for b in binary:
        if b == '1':
            max_ = max(max_, cnt)
            cnt = 0
        else:
            cnt += 1
    return max_

N = 1041
print(solution(N))