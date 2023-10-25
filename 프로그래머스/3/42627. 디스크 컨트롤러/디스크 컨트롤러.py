def solution(jobs):
    import heapq
    
    answer, i, now = 0, 0, 0
    start = -1
    jlist = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(jlist, [job[-1], job[0]])

        if len(jlist):
            cur = heapq.heappop(jlist)
            start = now
            now += cur[0]
            answer += now - cur[-1]
            i += 1
        else:
            now += 1
            
    answer = answer//len(jobs)
    return answer