def solution(my_string):
    answer = sum(int(num) for num in my_string.replace(" - "," + -").split(" + "))
    return answer