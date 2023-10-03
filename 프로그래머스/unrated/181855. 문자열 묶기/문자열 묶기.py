def solution(strArr):
    res=list(map(len, strArr))
    answer=max([res.count(num) for num in set(res)])
    return answer