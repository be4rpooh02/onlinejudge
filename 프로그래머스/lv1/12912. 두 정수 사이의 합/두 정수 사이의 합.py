def solution(a, b):
    m,n = max(a,b), min(a,b)
    answer = n*(m-n+1) + sum(range(m-n+1))

    return answer