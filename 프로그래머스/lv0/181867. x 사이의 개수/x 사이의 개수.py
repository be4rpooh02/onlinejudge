def solution(myString):
    arr=myString.split("x")
    answer = list(map(len, arr))
    return answer