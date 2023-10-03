def solution(my_string):
    answer = sum([int(num) for num in my_string if(num.isdigit())])
    return answer