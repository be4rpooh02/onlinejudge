def solution(myString):
    answer = sorted(filter(lambda x: x, myString.split("x")))
    return answer