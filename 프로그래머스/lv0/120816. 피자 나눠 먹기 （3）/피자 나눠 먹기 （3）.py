def solution(slice, n):
    answer = n//slice+bool(n%slice)
    return answer