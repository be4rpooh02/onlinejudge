def solution(a, b):
    res=int(str(a)+str(b))
    answer = res if(res>2*a*b) else 2*a*b
    return answer