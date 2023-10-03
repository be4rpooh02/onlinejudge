def solution(arr, query):
    answer = arr.copy()
    
    for i,idx in enumerate(query):
        answer=answer[idx:] if(i%2) else answer[:idx+1]

    return answer