def solution(numbers):
    from itertools import permutations

    res = []
    answer = 0
    
    for i in range(1, len(numbers)+1):
        res += list(map(lambda x: int("".join(x)), set(permutations(list(numbers), i))))
    
    for i in set(res):
        if i < 2:
            continue
        
        end = int(i**0.5) + 1
        
        flag = True
        for j in range(2, end):
            if i % j == 0:
                flag = False
                break
        
        answer += 1 if flag else 0
                    
    return answer