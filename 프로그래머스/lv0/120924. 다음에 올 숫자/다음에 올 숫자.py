def solution(common):
    a,b,c = common[:3]
    
    if(b-a == c-b):
        answer = common[-1]+(b-a)
    else:
        answer = common[-1]*(b//a)
    return answer