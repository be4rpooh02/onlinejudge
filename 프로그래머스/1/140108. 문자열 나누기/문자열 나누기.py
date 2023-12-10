def solution(s):
    cnt = 0
    idy = 0
    answer = 0
    
    for idx, ch in enumerate(s):
        cnt += 1 if ch == s[idy] else -1
                    
        if not cnt:
            answer += 1
            idy = idx+1
    
    answer += 1 if cnt else 0
    
    return answer