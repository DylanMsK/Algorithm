# url = 'https://programmers.co.kr/learn/courses/30/lessons/60057'

def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        result, unit, cnt = '', s[:i], 1
        for j in range(i, len(s), i):
            if s[j:j+i] == unit:
                cnt += 1
            else:
                result += str(cnt)+unit if cnt > 1 else unit
                unit = s[j:j+i]
                cnt = 1
        result += str(cnt)+unit if cnt > 1 else unit
        answer = min(answer, len(result))
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))