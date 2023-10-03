def solution(arr, queries):
    answer = arr.copy()
    
    for s, e, k in queries:
        for idx in range(s,e+1):
            if(not idx%k):
                answer[idx]+=1

    return answer