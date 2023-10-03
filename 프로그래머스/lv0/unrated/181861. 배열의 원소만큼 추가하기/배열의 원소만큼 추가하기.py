def solution(arr):
    answer = []
    answer=sum(list(map(lambda x: [x]*x, arr)),[])
    return answer