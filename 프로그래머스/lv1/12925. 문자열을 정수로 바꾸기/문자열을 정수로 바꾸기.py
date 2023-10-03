def solution(s):
    # answer = eval(s)
    if(s[0] in ['-','+']):
        mul=1 if(s[0] == '+') else -1
        s = s[1:]
    else:
        mul=1
    
    res = sum([int(ch)*(10**idx) for idx, ch in enumerate(s[::-1])])
    
    answer = res*mul
    
    return answer