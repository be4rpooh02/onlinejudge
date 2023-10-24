def solution(bridge_length, weight, truck_weights):    
    from collections import deque
    
    answer = 0
    psum, bridge = 0, deque(0 for _ in range(bridge_length))
    trucks = deque(truck_weights)

    while trucks:        
        psum -= bridge.popleft()
        answer += 1        
        
        if psum + trucks[0] > weight:
            bridge.append(0)
            continue
        
        t = trucks.popleft()
        bridge.append(t)
        psum += t
    
    while bridge:
        answer += 1
        bridge.popleft()
    
    return answer