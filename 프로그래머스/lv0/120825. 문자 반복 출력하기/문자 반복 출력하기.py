def solution(my_string, n):
    answer = ''.join([ch*n for ch in my_string])
    return answer