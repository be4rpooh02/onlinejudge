def solution(arr):            
    answer = []
    
    for item in arr:
        if(item<50):
            answer.append(item*2) if(item%2) else answer.append(item)
        else:
            answer.append(item) if(item%2) else answer.append(item/2)
    return answer