def solution(n):
    """
    res=[]
    while(n>0):
        n,r = divmod(n,10)
        res.append(r)
    
    answer = sum([num*(10**idx) for idx, num in enumerate(sorted(res))])
    """
    answer = int(''.join(sorted(str(n), reverse=True)))
    return answer