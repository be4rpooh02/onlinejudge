def solution(price, money, count):
    res = sum([price*i for i in range(1,count+1)])
    answer = abs(money-res) if(res>money) else 0

    return answer