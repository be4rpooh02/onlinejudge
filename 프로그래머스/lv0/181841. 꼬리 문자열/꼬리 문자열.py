def solution(str_list, ex):
    res = ['' if(ex in item) else item for item in str_list]
    answer = ''.join(res)
    return answer