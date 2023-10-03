def solution(a, b):
    # gcd
    for i in range(min(a,b),0,-1):
        if(not a%i and not b%i):
            b=int(b/i)
            break

    # prime factorial
    if(b > 1):
        i, pf=2, []
        
        while(i<=b):
            if(not b%i):
                pf.append(i)
                b=b/i
            else:
                i=i+1 
        
        # pf가 2, 5의 부분집합이면 기약분수
        answer = 1 if(not set(pf)-set([2, 5])) else 2
    else:
        # 분모가 1이면 정수이므로 기약분수
        answer = 1
    return answer