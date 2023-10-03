def solution(n, m, section):
    s = section[0]
    answer=1
    
    for idx in section:
        if idx>=s and idx<=s+m-1:
            continue

        answer+=1
        s=idx if idx+m<=n else n-m+1
    
    return answer