def solution(n, m):
    a = n*m
    while(m>0):
        n,m = m, n%m
    
    answer = [n, a//n]
    return answer