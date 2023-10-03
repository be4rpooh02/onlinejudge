def solution(a, d, included):
    arr=zip(range(a,a+d*len(included), d), included)
    
    answer = sum([item[0] for item in arr if(item[1])])
    return answer