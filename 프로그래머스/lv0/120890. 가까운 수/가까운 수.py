def solution(array, n):
    answer = min(sorted([(abs(i-n),i) for i in array]))[-1]
    return answer