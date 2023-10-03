def solution(n):
    res = []
    for i in range(4, n+1):
        res.append(len([j for j in range(1,i+1) if not i%j]) >= 3)
    
    answer = sum(res)
    return answer