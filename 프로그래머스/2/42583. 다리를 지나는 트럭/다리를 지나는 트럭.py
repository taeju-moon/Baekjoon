def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    while truck_weights:
        bridge.pop(0)
        if (weight >= sum(bridge) + truck_weights[0]):
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

        answer += 1

    count = 0
    for index, data in enumerate(bridge):
        if data != 0: count = index + 1

    answer += count
    return answer