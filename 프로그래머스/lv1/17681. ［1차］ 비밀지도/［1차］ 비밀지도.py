def solution(n, arr1, arr2):
    res = [bin(a|b)[2:] for a,b in zip(arr1,arr2)]
    
    answer = []
    for s in res:
        if(len(s)<n):
            # rjust or zfill 사용 가능
            s = "0"*(n-len(s)) + s
        answer.append(s.replace("1","#").replace("0", " "))
    
    return answer