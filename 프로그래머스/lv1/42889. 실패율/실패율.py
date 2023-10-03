def solution(N, stages):
    res = [0]*(N+2)
    num = 0
    
    for i in stages:
        res[i]+=1
        num+=1
        
    for j,n in enumerate(res):
        res[j] = (j,n/num) if num>0 else (j,0)
        num-=n
    
    answer= [k[0] for k in sorted(res[1:-1],reverse=True,key=lambda x: x[1])]
    return answer