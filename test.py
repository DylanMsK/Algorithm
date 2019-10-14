def solution(routes):
    answer = []
    routes.sort(key=lambda x: (x[0], x[1]))
    _, move_out = routes[0]
    for i in range(1, len(routes)):
        if routes[i][0] > move_out:
            answer.append(i)
            _, move_out = routes[i]
        else:
            move_out = min(routes[i][1], move_out)

    if answer[-1] != len(routes):
        return len(answer)+1
    return len(answer)


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))