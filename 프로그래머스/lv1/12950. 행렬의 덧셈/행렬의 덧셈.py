def solution(arr1, arr2):
    answer = [[m+n for m,n in zip(a,b)] for a,b in zip(arr1, arr2)]
    #answer = []
    #for a,b in zip(arr1, arr2):
    #    res = []
    #    for m,n in zip(a,b):
    #        res.append(m+n)
    #    answer.append(res)
    return answer