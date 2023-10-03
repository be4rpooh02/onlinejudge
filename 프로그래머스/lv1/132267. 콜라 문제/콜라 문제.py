def solution(a, b, n):
    answer = 0
    while(n>=a):
        v,m = divmod(n,a)
        
        answer += v*b
        n = m+v*b
        
    return answer