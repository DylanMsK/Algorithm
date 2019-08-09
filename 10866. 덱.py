# url = 'https://www.acmicpc.net/problem/10866'
import sys
N = int(sys.stdin.readline())
q, length = [], 0

for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        q = [cmd[1]] + q
        length += 1
    elif cmd[0] == 'push_back':
        q = q + [cmd[1]]
        length += 1
    elif cmd[0] == 'pop_front':
        if length:
            sys.stdout.write(q.pop(0)+'\n')
            length -= 1
        else:
            sys.stdout.write('-1'+'\n')
    elif cmd[0] == 'pop_back':
        if length:
            sys.stdout.write(q.pop()+'\n')
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
    elif cmd[0] == 'front':
        if length:
            sys.stdout.write(q[0]+'\n')
        else:
            sys.stdout.write('-1'+'\n')
    else:
        if length:
            sys.stdout.write(q[-1]+'\n')
        else:
            sys.stdout.write('-1'+'\n')
