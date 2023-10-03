def solution(n):
    answer = (n**0.5+1)**2 if(not (n**0.5)%1) else -1
    return answer