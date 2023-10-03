def solution(arr):
    n=len(arr)
    
    answer=1
    
    for i in range(1,n):
        for j in range(i):
            if(arr[i][j] != arr[j][i]):
                answer=0
                break
        
        if(not answer):
            break

    return answer