a, b = map(int, input().strip().split())
consumers = [0]*b
messages = [int(input()) for _ in range(a)]

time, flag = 0, False
while 1:
    for idx in range(b):
        if consumers[idx] == 0:
            if messages:
                consumers[idx] = messages.pop(0)
            else:
                flag = True
                break

    if flag:
        time += max(consumers)
        break

    spent = min(consumers)
    for idx in range(b):
        consumers[idx] -= spent
    time += spent

print(time)