def solution(n):
    answer = 1 if(int(n**(1/2))**2 == n) else 2
    return answer