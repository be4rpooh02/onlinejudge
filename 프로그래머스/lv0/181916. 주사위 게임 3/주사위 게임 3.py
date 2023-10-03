def solution(a, b, c, d):
    abcd = [a, b, c, d]
    cnts = [abcd.count(x) for x in abcd]
    
    if(max(cnts) == 4):
        answer=a*1111
    elif(max(cnts) == 3):
        p = abcd[cnts.index(3)]
        q = abcd[cnts.index(1)]
        answer=(10*p + q)**2
    elif(max(cnts) == 2):
        if(min(cnts)==1):
            p=abcd[cnts.index(2)]**2
            answer=(a*b*c*d)/p
        else:
            answer = (a+b)*abs(a-b) if(a==c) else (a+c)*abs(a-c)
    else:
        answer=min(abcd)
    
    return answer