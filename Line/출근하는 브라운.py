n = int(input().strip())
seats = list(map(int, input().strip().split()))
close = 0

if sum(seats) == 1:
    for i in range(n):
        if seats[i]:
            idx = i
            break

    close = max(idx-0, n-1-idx)

else:
    for i in range(n):
        if seats[i]:
            close = max(i, close)
            break

    for i in range(n):
        if seats[i]:
            for j in range(i+1, n):
                if seats[j]:
                    distance = j-i
                    close = max(distance // 2, close)
                    break
            else:
                distance = n-1-i
                close = max(distance, close)
                break
print(close)