def solution(my_strings, parts):
    res = [item[0][item[1][0]:item[1][1]+1] for item in zip(my_strings, parts)] 
    answer = ''.join(res)
    return answer