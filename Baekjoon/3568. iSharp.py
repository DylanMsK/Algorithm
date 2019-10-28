# url = 'https://www.acmicpc.net/problem/3568'

txt = input()[:-1]
comm, *vals = txt.split()
vals = ''.join(vals)
for val in vals.split(','):
    for i in range(len(val)):
        if val[i] == '[' or val[i] == '&' or val[i] == '*':
            name, left = val[:i], val[i:]
            break
    else:
        name, left = val, ''

    reform = ''
    for i in list(left)[::-1]:
        if i == ']':
            reform += '[]'
        elif i == '[':
            continue
        else:
            reform += i
    print(comm + reform, name + ';')
