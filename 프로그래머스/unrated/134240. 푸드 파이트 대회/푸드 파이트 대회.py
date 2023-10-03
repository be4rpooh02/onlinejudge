def solution(food):
    res = ''
    for idx, f in enumerate(food):
        if(f > 1):
            res += str(idx)*(f//2)
        
    answer = '0'.join([res, res[::-1]])
    return answer