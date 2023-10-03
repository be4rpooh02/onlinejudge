def solution(n):
    res=1
    for answer in range(1,11):   
        res*=answer
        if(res>n):
            answer-=1
            break     
    return answer