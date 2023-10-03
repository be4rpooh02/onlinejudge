def solution(arr):
    result, i = [], 0
    
    while(i<len(arr)):
        result.append(arr[i]) if(not result or result[-1] != arr[i]) else result.pop(-1)  
        i+=1  
    
    answer = result if(result) else [-1]
    
    return answer