def solution(arr):
    answer, prev = [arr[0]], arr[0]
    
    for num in arr:
        if(num != prev):
            answer.append(num)
        prev = num
        
    return answer