def solution(arr, flag):
    answer = []
    for idx, ch in enumerate(flag):
        if(ch):
            answer += [arr[idx]]*arr[idx]*2
        else:
            answer = answer[:arr[idx]*-1]
        
    return answer