def solution(my_string):
    answer = [0 for _ in range(52)]
    
    res = list(my_string)
    cnt = [(ch, res.count(ch)) for ch in set(my_string)]
    
    for ch, count in cnt:
        idx = ord(ch)-ord('A')-6 if(ch.islower()) else ord(ch)-ord('A')
        answer[idx]=count
    
    return answer