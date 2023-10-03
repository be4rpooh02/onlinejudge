def solution(balls, share):
    bf,sf,bsf = 1,1,1
    
    for num in range(balls, 0, -1):
        bf*=num
    
    for num in range(share, 0, -1):
        sf*=num
    
    for num in range(balls-share, 0, -1):
        bsf*=num
    
    answer = bf / (sf*bsf)
    return answer