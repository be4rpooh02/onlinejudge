def solution(arr, queries):
    answer = []
    
    for s,e,k in queries:
        res =[num for num in arr[s:e+1] if(num>k)]
        answer.append(min(res)) if(res) else answer.append(-1)

    return answer