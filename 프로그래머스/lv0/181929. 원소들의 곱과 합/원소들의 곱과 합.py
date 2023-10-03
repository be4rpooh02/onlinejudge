def solution(num_list):
    res_mul=1
    res_sum=0
    for num in num_list:
        res_mul*=num
        res_sum+=num
    
    answer = 1 if res_mul<(res_sum**2) else 0
    return answer