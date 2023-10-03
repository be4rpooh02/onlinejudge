def solution(babbling):
    import re
    
    answer=0
    pat = re.compile("^(aya|ye|woo|ma)")
    
    for word in babbling:
        prev=""
        
        while word:
            res = re.search(pat, word)
            w = res.group() if res else 0
            
            if not res or w==prev:
                break
                
            prev = w
            word = re.sub(pat, "", word)
        
        answer+=1 if not word else 0

    return answer