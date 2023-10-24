def solution(prices):
    answer = [0] * len(prices)
    s = []
    
    for idx, price in enumerate(prices):
        if not s or prices[s[-1]] < price:
            s.append(idx)
            continue    

        while s and price < prices[s[-1]]:
            t = s.pop(-1)
            answer[t] = idx - t

        s.append(idx)

    print(s)
        
    for item in s:
        answer[item]= len(prices) - item - 1                
    return answer