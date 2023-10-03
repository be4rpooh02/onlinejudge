def solution(l, r):
    res = [num for num in range(l,r+1) if(not str(num).replace("5","").replace("0","")) ]
    answer = res if(res) else [-1]

    return answer