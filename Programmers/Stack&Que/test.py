def solution(tickets):
    routes = {}
    for ticket in tickets:
        if ticket[0] in routes:
            routes[ticket[0]].append(ticket)
        else:
            routes[ticket[0]] = [ticket]
            
    answer = [[city] for city in routes['ICN']]
    tot = len(tickets)-1
    while 1:
        nxt = []
        while answer:
            route = answer.pop(0)
            final_city = route[-1][-1]
            for city in routes[final_city]:
                if city not in route:
                    nxt.append(route+[city])
        tot -= 1
        if tot == 0:
            break
        answer = nxt
    
    if len(answer) == 1:
        return nxt[0]
    else:
        answer = []
        for route in nxt:
            temp = ['ICN']
            for i in route:
                temp.append(i[1])
            answer.append(temp)

        return sorted(answer)[0]

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])