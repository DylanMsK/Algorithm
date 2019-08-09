# url = 'https://www.acmicpc.net/problem/10828'
import sys

N = int(sys.stdin.readline())
s, length = [], 0
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        s = s + [cmd[1]]
        length += 1
    elif cmd[0] == 'pop':
        if length:
            sys.stdout.write(s.pop()+'\n')
            length -= 1
        else:
            sys.stdout.write('-1'+'\n')
    elif cmd[0] == 'size':
        sys.stdout.write(str(length)+'\n')
    elif cmd[0] == 'empty':
        if length:
            sys.stdout.write('0'+'\n')
        else:
            sys.stdout.write('1'+'\n')
    else:
        if length:
            sys.stdout.write(s[-1]+'\n')
        else:
            sys.stdout.write('-1'+'\n')