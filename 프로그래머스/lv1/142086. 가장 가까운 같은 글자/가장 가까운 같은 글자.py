def solution(s):
    answer, res = [], {}
    
    for i,ch in enumerate(s):
        if(ch in res.keys()):
            answer.append(i-res[ch])
        else:
            answer.append(-1)
        
        res[ch] = i  
    return answer