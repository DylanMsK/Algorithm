def check_right(u):
    temp = []
    for i in u:
        if i == '(':
            temp.append(i)
        else:
            if temp[-1] == '(':
                temp.pop()
            else:
                return False
    return True


def solution(p):
    answer = ''
    
    # 1.
    if p == '':
        return p
    # 2.
    temp = []
    for i in range(len(p)):
        if p[i] == '(':
            temp.append(p[i])
        else:
            if len(temp) == 0:
                temp.append(p[i])
                continue
            if temp[-1] == '(':
                temp.pop()
                if len(temp) == 0:
                    u, v = p[:i+1], p[i+1:]
                    break
    # 3.
    if check_right(u):
        # 3-1.
        u += solution(v)
        return u
        
    # 4.
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        answer += u[1:-1][::-1]
        return answer

print(solution(")("))