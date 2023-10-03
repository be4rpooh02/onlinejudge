def solution(num, total):
    c = total//num
    s = c-num//2 if(num%2) else c-num//2+1
    e = c+num//2+1
    answer=list(range(s,e))

    return answer