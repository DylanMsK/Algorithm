# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIsY84KEPMDFAWN&categoryId=AWIsY84KEPMDFAWN&categoryType=CODE'

for tc in range(int(input())):
    deck = {'S': [0]*13,
            'D': [0]*13,
            'H': [0]*13,
            'C': [0]*13}
    cards = input()
    flag = True
    for i in range(0, len(cards), 3):
        if not deck[cards[i]][int(cards[i+1:i+3])-1]:
            deck[cards[i]][int(cards[i+1:i+3])-1] += 1
        else:
            flag = False
            break
    if flag:
        result = []
        for k in deck:
            result.append(str(deck[k].count(0)))
        result = ' '.join(result)
    else:
        result = 'ERROR'
    print(f'#{tc+1} {result}')