def solution(numbers, n):
    answer = 0
    tmp_nums = numbers.copy()
    
    while(answer <= n):
        answer+=tmp_nums.pop(0)
    
    return answer