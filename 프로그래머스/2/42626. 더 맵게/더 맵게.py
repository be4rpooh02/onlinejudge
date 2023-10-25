def solution(scoville, K):
    import heapq

    heapq.heapify(scoville)
    answer = 0
    
    while True:
        f = heapq.heappop(scoville)
        
        if f >= K:
            break

        if not scoville:
            answer = -1
            break
        
        s = heapq.heappop(scoville)
        res = f + s * 2
        heapq.heappush(scoville, res)
        answer += 1
        
    return answer