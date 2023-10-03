def solution(k, m, score):
    answer = sum(sorted(score)[len(score)%m::m])*m
    
    return answer