def check(x, y):
    s, b = 0, 0
    for i in range(3):
        if y[i] == x[i]:
            s += 1
            continue
        if y[i] in x:
            b += 1
    return (s, b)


def solution(baseball):
    answer = 0
    for ball in baseball:
        ball[0] = str(ball[0])
    nums = []
    for i in range(100, 1000):
        num = str(i)
        if len(set(num)) == 3 and '0' not in num:
            nums.append(num)

    for x in nums:
        for ball in baseball:
            s, b = check(x, ball[0])
            if s != ball[1] or b != ball[2]:
                break
        else:
            answer += 1
            
    return answer
