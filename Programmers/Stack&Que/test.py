bridge_length = 100
weight = 100
truck_weights = [10]


# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     done, doing = [], []
#     print(f'경과 시간: {answer}, 대기중: {truck_weights}, 지나간 트럭: {done}, 건너는 트럭: {doing}')
#     while 1:
#         if weight - truck_weights[0] >= 0:
#             answer += 1
#             truck = truck_weights.pop(0)
#             doing.append([0, truck])
#             weight -= truck
#             for truck in doing:
#                 truck[0] += 1
#             if doing[0][0] > bridge_length:
#                 weight += doing[0][1]
#                 done.append(doing.pop(0))
#         else:
#             spend = bridge_length+1 - doing[0][0]
#             for truck in doing:
#                 truck[0] += spend
#             answer += spend
#             truck = doing.pop(0)
#             weight += truck[1]
#             done.append(truck)
#             if weight - truck_weights[0] >= 0:
#                 truck = truck_weights.pop(0)
#                 doing.append([1, truck])
#                 weight -= truck

#         print(f'경과 시간: {answer}, 대기중: {truck_weights}, 지나간 트럭: {done}, 건너는 트럭: {doing}')

#         if not truck_weights:
#             answer += bridge_length+1 - doing[-1][0]
#             break

#     print(f'경과 시간: {answer}, 대기중: {truck_weights}, 지나간 트럭: {done}, 건너는 트럭: {doing}')

#     return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    going = []
    while 1:
        print(f'경과 시간: {answer}, 대기중: {truck_weights}, 건너는 트럭: {going}')
        answer += 1
        for truck in going:
            truck[0] += 1
        if going and going[0][0] > bridge_length:
            truck = going.pop(0)
            weight += truck[1]

        if weight - truck_weights[0] >= 0:
            truck_weight = truck_weights.pop(0)
            weight -= truck_weight
            going.append([1, truck_weight])
        else:
            spend = bridge_length - going[0][0]
            answer += spend
            for truck in going:
                truck[0] += spend
        if not truck_weights:
            answer += bridge_length+1 - going[-1][0]
            break
            
    print(f'경과 시간: {answer}, 대기중: {truck_weights}, 건너는 트럭: {going}')





    return answer

solution(bridge_length, weight, truck_weights)