def solution(n):
    """
    answer=0
    
    for i in range(2,n+1):
        for j in range(2,int(i**0.5) + 1):
            if i%j==0:
                break
        else:
            answer+=1
    """
    a=set(range(3,n+1,2))
    for i in range(3,n+1,2):
        if i in a:
            a-=set(range(i*2,n+1,i))
            
    answer=len(a)+1
    

    return answer