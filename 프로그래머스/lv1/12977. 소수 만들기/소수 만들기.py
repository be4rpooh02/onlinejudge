def solution(nums):
    from itertools import combinations
    
    answer=0
    res = []
    
    for items in list(combinations(nums, 3)):
        s=sum(items)
        for i in range(2,s//2):
            if not s%i:
                break
        else:
            answer+=1
    return answer