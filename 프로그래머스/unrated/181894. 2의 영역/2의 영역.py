def solution(arr):
    idx = [idx for idx, num in enumerate(arr) if(num==2)]    
    answer = arr[min(idx):max(idx)+1] if(len(idx)) else [-1]
    
    return answer