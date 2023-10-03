def solution(num_list):
    even, odd = "", ""
    
    for item in num_list:
        if(item%2):
            odd=odd+str(item)
        else:
            even=even+str(item)
    answer = int(odd)+ int(even)
    return answer