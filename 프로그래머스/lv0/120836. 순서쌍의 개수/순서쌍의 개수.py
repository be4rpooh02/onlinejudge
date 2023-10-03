def solution(n):
    answer = sum(map(lambda x: 0 if(n%x) else 1, range(1,n+1)))
    return answer