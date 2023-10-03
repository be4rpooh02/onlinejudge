def solution(number, n, m):
    answer = 1 if not number%n and not number%m else 0
    return answer