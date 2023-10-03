def solution(my_string):
    res=""
    for ch in my_string:
        res = res+(ch if(ch.isdigit()) else " ")
    
    answer = sum(int(num) for num in res.split())
    return answer