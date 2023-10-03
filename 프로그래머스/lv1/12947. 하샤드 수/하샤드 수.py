def solution(x):
    res = sum(map(int, str(x)))
    answer = False if(x%res) else True
    return answer