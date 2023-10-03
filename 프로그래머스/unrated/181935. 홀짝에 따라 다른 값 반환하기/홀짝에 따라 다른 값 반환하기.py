def solution(n):
    answer = sum(list(range(1, n+1, 2))) if(n%2) else sum(list(item**2 for item in range(0, n+1, 2)))
    return answer