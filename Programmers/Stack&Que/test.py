def solution(begin, target, words, answer=0):
    if begin == target:
        return answer
    if not words:
        return 0
    print(begin, target, words)
    l = len(begin)
    promiss = []
    for word in words:
        cnt = 0
        for i in range(l):
            if cnt > 1:
                break
            if word[i] == begin[i]:
                cnt += 1
        if cnt == 1:
            promiss.append(word)

    print(f"answer: {answer}, promiss: {promiss}")
    while promiss:
        word = promiss.pop(0)
        solution(word, target, [i for i in words if i != word], answer+1)
    

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))