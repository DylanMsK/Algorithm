def solution(lines):
    logs = []
    for line in lines:
        _, done, time = line.split()
        h, m, s = done.split(':')
        end = (int(h)*60*60 + int(m)*60 + float(s))*1000
        logs.append((end-float(time[:-1])*1000+1, end))
    stack = [logs[0]]
    max_ = 1
    for log in logs[1:]:
        if log[0] - stack[0][1] < 1000:
            stack.append(log)
            max_ = max(max_, len(stack))
        else:
            stack.pop(0)
            while stack:
                if log[0] - stack[0][1] < 1000:
                    break
                stack.pop(0)
            stack.append(log)
    return max_