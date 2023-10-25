def solution(operations):
    import heapq
    
    answer = []
    
    for item in operations:
        m, v = item.split(" ")
        
        if m == "I":
            heapq.heappush(answer, int(v))
        
        if m == "D" and answer:
            if v == "-1":
                heapq.heappop(answer)
            if v == "1":
                answer.pop(-1)
            
    if answer:
        answer = [max(answer), heapq.heappop(answer)]
    else:
        answer = [0, 0]
    
    return answer