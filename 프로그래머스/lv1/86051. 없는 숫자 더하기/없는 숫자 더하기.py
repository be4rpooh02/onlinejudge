def solution(numbers):
    answer = sum(set(range(10)).difference(set(numbers)))
    return answer