def solution(array, height):
    answer = sum([item>height for item in array])
    return answer