def solution(numer1, denom1, numer2, denom2):
    res=[numer1*denom2+numer2*denom1, denom1*denom2]
    
    m,n = res
    while(m>0):
        n,m = m, n%m

    answer = [res[0]//n, res[1]//n]
    return answer