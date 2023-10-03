def solution(num_list, n):
    ids=list(range(0,len(num_list),n))
    
    answer = [num_list[id] for id in ids]
    return answer