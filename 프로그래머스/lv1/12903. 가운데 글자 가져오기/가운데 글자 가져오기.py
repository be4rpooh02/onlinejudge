def solution(s):
    #is_odd = len(s)%2
    #c = len(s)//2
    #answer = s[c] if(is_odd) else s[c-1:c+1]
    answer = s[(len(s)-1)//2:len(s)//2+1]
    return answer