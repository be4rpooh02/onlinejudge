def solution(array):
    m,p=0,0
    for idx,i in enumerate(array):
        if(i>m):
            m,p = i,idx
    
    answer=[m,p]
    #m=max(array)
    #answer = [m, array.index(m)]
    return answer