from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    cur_road = deque()
    cur_weight = 0
    time = 0
    
    while truck_weights:
        if cur_weight + truck_weights[0] <= weight and len(cur_road) < bridge_length:
            truck = truck_weights.popleft()
            cur_weight += truck
            cur_road.append((truck, time))
            time += 1
            if time - cur_road[0][1] == bridge_length:
                cur_weight -= cur_road.popleft()[0]
        else:
            end_truck = cur_road.popleft()
            cur_weight -= end_truck[0]
            plus = bridge_length - (time - end_truck[1])
            time += plus
    if cur_road:
        end_truck = cur_road.pop()
        plus = bridge_length - (time - end_truck[1])
        time += plus

    answer= time + 1
    return answer