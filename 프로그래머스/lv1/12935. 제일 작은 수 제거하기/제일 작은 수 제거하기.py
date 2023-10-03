def solution(arr):
    res = arr.copy()
    res.remove(min(res))
    answer = res if(res) else [-1]
    return answer