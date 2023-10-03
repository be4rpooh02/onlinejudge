def solution(chicken):
    coupon,answer = chicken,0
    
    while(coupon>=10):
        service, coupon = divmod(coupon, 10)
        answer += service
        coupon += service    

    return answer