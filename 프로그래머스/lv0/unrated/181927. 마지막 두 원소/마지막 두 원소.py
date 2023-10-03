def solution(num_list):
    res = num_list[-1]-num_list[-2] if(num_list[-1]>num_list[-2]) else num_list[-1]*2
    answer = num_list.copy()
    answer.append(res)
    return answer