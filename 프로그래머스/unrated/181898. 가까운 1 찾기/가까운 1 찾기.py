def solution(arr, idx):
    answer = [n for n in range(idx,len(arr)) if(arr[n])]
    return answer[0] if(len(answer)) else -1