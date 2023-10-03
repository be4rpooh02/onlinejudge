def solution(my_string):
    res = [int(ch) for ch in my_string if(ch.isdigit())]
    answer = sorted(res)
    return answer