def solution(citations):
    n = len(citations)
    cs = sorted(citations, reverse = True)
    answer = 0
    
    for i in range(n, 0, -1):
        if cs[0] < i:
            continue
        
        h = 0
        
        for c in cs:
            if c >= i:
                h+=1
            else:
                break
        
        if h >= i:
            answer = i
            break
    
    return answer
