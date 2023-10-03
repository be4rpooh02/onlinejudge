def solution(n):
    answer = 0
    for i in range(max(6,n),6*n+1):
        if not i%6 and not i%n:
            answer = i//6
            break
    
    return answer