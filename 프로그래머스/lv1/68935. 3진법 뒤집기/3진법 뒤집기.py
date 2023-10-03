def solution(n):
    res = ''
    while(n>0):
        n,r = divmod(n,3)
        res+=str(r)
    
    #answer = sum(int(ch)*(3**idx) for idx, ch in enumerate(res[::-1]))
    answer = int(res, 3)

    return answer