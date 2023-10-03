def solution(number, limit, power):
    answer=0
    for num in range(1,number+1):
        res = 0
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                res+=1
                if(i**2 < num):
                    res+=1
        if res>limit:
            answer+=power
        else:
            answer+=res
        
    return answer