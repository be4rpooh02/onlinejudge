def solution(d, budget):
    answer = 0
    dep = sorted(d)
    res = 0
    
    while(len(dep)>0):
        res+=dep[0]
        if(res<=budget):
            dep.remove(dep[0])
            answer+=1
        else:
            break

    return answer