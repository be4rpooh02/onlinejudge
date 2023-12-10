def solution(s):
    xcnt, ycnt = 0, 0
    x = None
    slen = len(s) - 1
    answer = 0
    
    for idx, ch in enumerate(s):
        if not xcnt:
            x = ch
            xcnt += 1
            continue
            
        if ch == x:
            xcnt += 1
            continue

        if x != ch:
            ycnt += 1
            
            if ycnt == xcnt:
                answer += 1
                x = ""
                xcnt, ycnt = 0, 0
    
    if xcnt != ycnt:
        answer += 1
    
    return answer