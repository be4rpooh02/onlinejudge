def solution(a, b):
    answer = sum([m*n for m,n in zip(a,b)])
    return answer