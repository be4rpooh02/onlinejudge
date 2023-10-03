def solution(a, b, c):
    n = len(set([a,b,c]))
    
    if(n==3):
        answer=sum([a,b,c]) 
    elif(n==2):
        answer=sum([a,b,c])*sum([a**2,b**2,c**2])
    else:
        answer=sum([a,b,c])*sum([a**2,b**2,c**2])*sum([a**3,b**3,c**3])
        
    return answer