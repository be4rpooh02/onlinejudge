def solution(my_string):
    answer = ''.join([ch for ch in my_string if(ch not in ['a','e','i','o','u'])])
    return answer