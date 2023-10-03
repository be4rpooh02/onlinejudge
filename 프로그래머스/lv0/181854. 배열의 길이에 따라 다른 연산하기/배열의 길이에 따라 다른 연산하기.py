def solution(arr, n):
    answer=[]
    iter = range(0,len(arr),2) if(len(arr)%2) else range(1,len(arr),2)

    for item in enumerate(arr):
        if(item[0] in iter):
            answer.append(item[1]+n)
        else:
            answer.append(item[1])

    return answer