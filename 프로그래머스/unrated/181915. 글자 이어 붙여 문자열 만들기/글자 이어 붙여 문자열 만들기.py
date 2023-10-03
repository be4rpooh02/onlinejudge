def solution(my_string, index_list):
    
    answer=''.join(list(map(lambda x: my_string[x], index_list)))
    return answer