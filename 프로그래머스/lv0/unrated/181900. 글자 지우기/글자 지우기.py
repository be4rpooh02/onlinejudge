def solution(my_string, indices):
    set_ids = set(indices)
    answer = ''.join([ch for idx, ch in enumerate(my_string) if(idx not in set_ids)])
    return answer