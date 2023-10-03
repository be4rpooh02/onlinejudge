def solution(arr, queries):
    answer = arr.copy()
    
    for num in queries:
        for i in range(num[0],num[1]+1):
            answer[i]+=1

    return answer