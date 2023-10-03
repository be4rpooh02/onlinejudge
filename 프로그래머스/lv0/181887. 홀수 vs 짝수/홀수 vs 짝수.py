def solution(num_list):
    even, odd = 0, 0
    
    for item in enumerate(num_list):
        if(item[0]%2):
            even+=item[1]
        else:
            odd+=item[1]
    
    answer = max(odd, even)
    return answer