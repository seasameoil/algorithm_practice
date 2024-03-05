from collections import deque

def solution(bridge_length, weight, truck_weights):
    dq = deque()
    n = len(truck_weights)
    cnt = 0
    time = 0
    s_weight = 0
    
    while cnt != n:
        time += 1
        if truck_weights and s_weight+truck_weights[0] <= weight:
            x = truck_weights.pop(0)
            dq.append(x)
            s_weight += x
        else:
            dq.append(0)
        
        if len(dq) == bridge_length and dq[0] != 0:
            s_weight -= dq.popleft()
            cnt += 1
        elif len(dq) == bridge_length and dq[0] == 0:
            dq.popleft()
    
    return time+1