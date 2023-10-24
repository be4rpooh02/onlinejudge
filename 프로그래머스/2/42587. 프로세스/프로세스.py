def solution(priorities, location):
    from collections import deque
    
    target = (priorities[location], location)
    tp = deque((p, idx) for idx, p in enumerate(priorities))
    answer = 0
    
    while(tp):
        p = tp.popleft()
        
        if any(p[0] < t[0] for t in tp):
            tp.append(p)
        else:
            answer += 1
            
            if p[-1] == target[-1]:
                break
        
    return answer