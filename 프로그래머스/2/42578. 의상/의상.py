def solution(clothes):
    wears = {}
    comb = 1
    
    for cloth in clothes:
        if not wears.get(cloth[-1]):
            wears[cloth[-1]] = 1
        else:
            wears[cloth[-1]] += 1
            
    for cloth in wears.keys():
        comb = comb*(wears[cloth]+1)
    
    answer = comb - 1 if len(wears.keys()) > 1 else len(clothes)
    
    return answer