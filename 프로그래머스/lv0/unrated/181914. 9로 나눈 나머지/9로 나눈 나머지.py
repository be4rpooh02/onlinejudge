def solution(number):
    answer = sum(list(map(int, number.split())))%9
    return answer