# url = 'https://www.acmicpc.net/problem/4949'

while 1:
    string = input()
    if string == '.':
        break
    
    flag = True
    stack = []
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif i == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
    
    if flag and not len(stack):
        print('yes')
    else:
        print('no')