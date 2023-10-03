def solution(s):
    answer, idx = '', 0
    
    for ch in s:
        if(not ch.strip()):
            answer+=ch
            idx = 0
            continue
        
        answer+=ch.lower() if(idx%2) else ch.upper()
        idx+=1
        
    return answer